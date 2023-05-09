from flask import flash
from datetime import date, datetime
from flask_app.config.mysqlconnection import connectToMySQL;

class User:
    def __init__(self, data):
        self.id = data['id'];
        self.firstName = data['firstName'];
        self.lastName = data['lastName'];
        self.email = data['email'];
        self.birthday = data['birthday'];
        self.password = data['password'];
        self.createdAt = data['createdAt'];
        self.updatedAt = data['updatedAt'];

    @staticmethod
    def validate_user(user):
        # print (user);
        is_valid = True;
        if len(user['firstName']) < 2:
            flash("First name must be at least 2 characters.");
            is_valid = False;
        if len(user['lastName']) < 2:
            flash("Last name must be at least 2 characters.");
            is_valid = False;
        if len(user['email']) < 5:
            flash("Email must be at least 5 characters.");
            is_valid = False;
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.");
            is_valid = False;
        if user['birthday'] == "":
            flash("Birthday must be entered.");
            is_valid = False;
        
        newBirthday = datetime.strptime(user['birthday'], "%Y-%m-%d");

        #< This "should" convert the users birthday to be under or over 21   
        def calculate_age():
            today = date.today();
            # print(today.year);
            # print(newBirthday);
            age = today.year - newBirthday.year - ((today.month, today.day) < (newBirthday.month, newBirthday.day));
            return age;
        
        age = calculate_age();
        
        if age < 21:
            flash("Must be 21 years or older to register.");
            is_valid = False;
        return is_valid;

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;";
        results = connectToMySQL('whiskeybarrel').query_db(query);
        users = [];
        for user in results:
            users.append(cls(user));
        return users;

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (firstName, lastName, email, birthday, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(birthday)s ,%(password)s);";
        return connectToMySQL('whiskeybarrel').query_db(query, data);

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;";
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        if len(results) < 1:
            return False;
        return cls(results[0]);

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;";
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        if len(results) < 1:
            return False;
        return cls(results[0]);

    @classmethod
    def get_user_whiskey(cls, data):
        query = "SELECT * FROM whiskies JOIN personalWhiskey ON whiskies.id = personalWhiskey.whiskeyId WHERE personalWhiskey.userId = %(id)s AND personalWhiskey.wishList = 0;";
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        print(results);
        if len(results) < 1:
            return False;
        return results;

    @classmethod
    def get_user_wish(cls, data):
        query = "SELECT * FROM whiskies JOIN personalWhiskey ON whiskies.id = personalWhiskey.whiskeyId WHERE personalWhiskey.userId = %(id)s AND personalWhiskey.wishList = 1";
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        print(results);
        if len(results) < 1:
            return False;
        return results;