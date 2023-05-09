from flask_app import app;
from flask import jsonify, render_template, redirect, request, session, Flask;

from flask_app.models.whiskey import Whiskey;

@app.route("/create/whiskey", methods=["POST"])
def create_whiskey():
    data = {
        "name": request.form["name"],
        "distiller": request.form["distiller"],
        "age": request.form["age"],
        "country": request.form["country"],
        "dateTried": request.form["dateTried"],
        "style": request.form["style"],
        "proof": request.form["proof"],
        "price": request.form["price"],
        "rating": request.form["rating"],
        "notes": request.form["notes"],
    };

    if not Whiskey.validate_whiskey(request.form):
        return redirect("/whiskey/new");

    whiskey_id = Whiskey.save(data);

    return redirect(f"/dashboard");

@app.route("/create/wish", methods=["POST"])
def create_wish():
    data = {
        "user_id": session["user_id"],
        "name": request.form["name"],
        "distiller": request.form["distiller"],
        "age": request.form["age"],
        "country": request.form["country"],
        "style": request.form["style"],
        "proof": request.form["proof"],
        "price": request.form["price"],
        "notes": request.form["notes"],
    };

    Whiskey.saveWish(data);

    return redirect("/wishlist");

@app.route("/view/whiskey/<int:whiskey_id>")
def view_whiskey(whiskey_id):
    data = {
        "id": whiskey_id,
    };

    whiskey = Whiskey.get_by_id(data);

    return render_template("view.html", whiskey=whiskey);

@app.route("/edit/whiskey/<int:whiskey_id>")
def edit_whiskey(whiskey_id):
    data = {
        "id": whiskey_id,
    };

    whiskey = Whiskey.get_by_id(data);

    return render_template("edit.html", whiskey=whiskey);

@app.route("/update/whiskey/<int:whiskey_id>", methods=["POST"])
def update_whiskey(whiskey_id):
    data = {
        "name": request.form["name"],
        "distiller": request.form["distiller"],
        "age": request.form["age"],
        "country": request.form["country"],
        "dateTried": request.form["dateTried"],
        "style": request.form["style"],
        "proof": request.form["proof"],
        "price": request.form["price"],
        "rating": request.form["rating"],
        "notes": request.form["notes"],
        "wishList": request.form["wishList"],
        "id": whiskey_id,
        "userId": session["user_id"]
    };

    if(data['wishList'] == '1'):
        data['dateTried'] = "1000-01-01";
        data["rating"] = False;
    
    whiskey = Whiskey.update(data);
    return redirect("/dashboard");

@app.route("/delete/whiskey/<int:whiskey_id>")
def delete_whiskey(whiskey_id):
    data = {
        "id": whiskey_id,
    };

    Whiskey.delete(data);

    return redirect("/dashboard");

