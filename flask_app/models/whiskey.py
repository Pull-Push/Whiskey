from flask_app.config.mysqlconnection import connectToMySQL;
from flask import flash, session;
from datetime import date, datetime; 


class Whiskey:
    def __init__(self, data):
        self.id = data['id'];
        self.name = data['name'];
        self.distiller = data['distiller'];
        self.country = data['country'];
        self.age = data['age'];
        self.proof = data['proof'];
        self.price = data['price'];
        self.style = data['style'];
        self.rating = data['rating'];
        self.notes = data['notes'];
        self.dateTried = data['dateTried'];
        self.createdAt = data['createdAt'];
        self.updatedAt = data['updatedAt'];


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM whiskeys;";
        results = connectToMySQL('whiskeybarrel').query_db(query);
        whiskeys = [];
        for whiskey in results:
            whiskeys.append(cls(whiskey));
        return whiskeys;


    @classmethod
    def save(cls, data):
        query = "INSERT INTO whiskies (name, distiller, country, age, proof, price, style) VALUES (%(name)s, %(distiller)s, %(country)s, %(age)s, %(proof)s, %(price)s, %(style)s);";
        resultsMain = connectToMySQL('whiskeybarrel').query_db(query, data);
    
        data['whiskeyId'] = resultsMain;
        data['userId'] = session['user_id'];
        data['wishList'] = 0;


        # print("the whiskey id is",resultsMain)
        # print("the userid is",session['user_id'])
    
        queryPersonal = "INSERT INTO personalWhiskey (whiskeyId, userId, rating, dateTried, wishList, notes) VALUES (%(whiskeyId)s, %(userId)s,%(rating)s,%(dateTried)s, %(wishList)s,%(notes)s);"
        resultsPersonal = connectToMySQL('whiskeybarrel').query_db(queryPersonal, data);
        return resultsPersonal;

    @classmethod
    def saveWish(cls, data):
        query = "INSERT INTO whiskies (name, distiller, country, age, proof, price, style) VALUES (%(name)s, %(distiller)s, %(country)s, %(age)s, %(proof)s, %(price)s, %(style)s);";
        resultsMain = connectToMySQL('whiskeybarrel').query_db(query, data);
    
        data['whiskeyId'] = resultsMain;
        data['userId'] = session['user_id'];
        data['wishList'] = 1;


        # print("the whiskey id is",resultsMain)
        # print("the userid is",session['user_id'])
    
        queryPersonal = "INSERT INTO personalWhiskey (whiskeyId, userId, wishList, notes) VALUES (%(whiskeyId)s, %(userId)s,%(wishList)s, %(notes)s);"
        resultsPersonal = connectToMySQL('whiskeybarrel').query_db(queryPersonal, data);
        return resultsPersonal;


    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM whiskies JOIN personalWhiskey ON whiskies.id = personalWhiskey.whiskeyId WHERE personalWhiskey.whiskeyId = %(id)s";
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        return cls(results[0]);

    @classmethod
    def update(cls, data):

        query = "UPDATE whiskies SET name = %(name)s, distiller = %(distiller)s, country = %(country)s, age = %(age)s, proof = %(proof)s, price = %(price)s, style = %(style)s WHERE id = %(id)s;"
        personalQuery = "UPDATE personalWhiskey SET wishList=%(wishList)s,rating = %(rating)s, notes = %(notes)s, dateTried = %(dateTried)s WHERE whiskeyId = %(id)s AND userId = %(userId)s;"

        print("the rating is",data['rating'])

        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        personalResults = connectToMySQL('whiskeybarrel').query_db(personalQuery, data);

        print("the whiskey id is",results)
        print("the userid is",session['user_id'])

        return results


    @classmethod
    def delete(cls, data):
        data['userId'] = session['user_id'];
        query = "DELETE FROM whiskies WHERE id = %(id)s;";
        deletePersonal = "DELETE FROM personalWhiskey WHERE whiskeyId = %(id)s AND userId = %(userId)s;";
        
        results = connectToMySQL('whiskeybarrel').query_db(query, data);
        personalResults = connectToMySQL('whiskeybarrel').query_db(deletePersonal, data);
        return results;

    @staticmethod
    def validate_whiskey(whiskey):
        is_valid = True;
        if len(whiskey['name']) < 2:
            flash("Name must be at least 2 characters.",'whiskerr');
            is_valid = False;
        if len(whiskey['distiller']) < 2:
            flash("Distiller must be at least 2 characters.",'whiskerr');
            is_valid = False;
        if len(whiskey['country']) < 2:
            flash("Country must be at least 2 characters.",'whiskerr');
            is_valid = False;
        if len(whiskey['age']) < 1:
            flash("Age must be at least 1 character.",'whiskerr');
            is_valid = False;
        if len(whiskey['proof']) < 1:
            flash("Proof must be at least 1 character.",'whiskerr');
            is_valid = False;
        if len(whiskey['price']) < 1:
            flash("Price must be at least 1 character.",'whiskerr');
            is_valid = False;
        if len(whiskey['style']) < 2:
            flash("Style must be at least 2 characters.",'whiskerr');
            is_valid = False;
        return is_valid;

