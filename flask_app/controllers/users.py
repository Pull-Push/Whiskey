from flask_app import app;
from flask import render_template, redirect, request, session, Flask;

from flask_app.models.user import User;

@app.route("/create/user", methods=["POST"])
def create_user():
    data = {
        "firstName": request.form["firstName"],
        "lastName": request.form["lastName"],
        "email": request.form["email"],
        "birthday": request.form["birthday"],
        "password": request.form["password"],
        "confirmPassword": request.form["confirmPassword"],
    };

    if not User.validate_user(request.form):
        return redirect("/");

    user_id = User.save(data);

    session["user_id"] = user_id;
    # print("users line 22 ", session["user_id"]);
    # print("User created successfully!");
    return redirect("/dashboard");

@app.route("/login/user", methods=["POST"])
def login_user():
    data = {
        "email": request.form["email"],
        "password": request.form["password"],
    };    
    if User.validate_log(data):
        user = User.get_by_email(data);
        session["user_id"] = user.id;
        return redirect("/dashboard");
    else:
        return redirect("/");

@app.route("/logout/user")
def logout_user():
    session.clear();
    return redirect("/");

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/");

    data = {
        "id": session["user_id"],
    };

    print("users line 55 userID", data);

    user = User.get_by_id(data);
    user_whiskey = User.get_user_whiskey(data);

    return render_template("dashboard.html", user=user, shelf=user_whiskey);

@app.route("/wishlist")
def wishlist():
    if "user_id" not in session:
        return redirect("/");

    data = {
        "id": session["user_id"],
    };

    print("users line 71 userID", data);
    
    user = User.get_by_id(data);
    user_wish = User.get_user_wish(data);
    print("users line 71 ", user_wish);

    return render_template("wishlist.html", user=user, wish=user_wish);
