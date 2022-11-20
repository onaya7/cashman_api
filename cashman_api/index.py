from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiating SQLAlchemy
db = SQLAlchemy(app)

# DATABASE MODELS
class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False )
    last_name = db.Column(db.String(80), unique=True, nullable=False )
    email = db.Column(db.String(120), unique=True, nullable=False )

    def __repr__(self):
        return '<User %r>' % self.first_name

# APPLICATION ROUTES

# Post request
class CreateUser(Resource):
    response = {"status" : 400, "message": "User not created"}

    def post(self):
        user_data = request.get_json()
        first_name = user_data["first_name"]
        last_name = user_data["last_name"]
        email = user_data["email"]
        user = User(first_name=first_name, last_name=last_name, email=email)
        db.session.add(user)
        db.session.commit()

        self.response["status"] = 201
        self.response["message"] = "User created sucessfully"

        return self.response, 201

api.add_resource(CreateUser, "/api/create")

# Get request
class Users(Resource):
    response = {"status": 404, "message" : "Users not available"}

    def get(self):
        # query to retrieve all users and store them in the users variable
        users = User.query.all()
        # if user exists in the database 
        if users:
            all_users = []
            # looping through all the users from the users variable query
            for user in users:
                user_details = {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }

                all_users.append(user_details)
            self.response["status"] = 200
            self.response["message"] = all_users
            return self.response, 200

        # if user does not exist in the database
        else:
            return self.response, 404
api.add_resource(Users, "/api/users")


# Get request that retrieves a single user using the user_id
class GetUser(Resource):
    response = {"status": 404, "message" : "Users not available"}
    
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
                user_details = {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
                self.response["status"] = 200
                self.response["message"] = user_details

                return self.response, 200
        else:
            return self.response, 404

api.add_resource(GetUser, "/api/user/<int:user_id>/")

# Put request
class UpdateUser(Resource):
    response = {"status": 404, "message": "Users not available"}

    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            user_data = request.get_json()
            first_name = user_data["first_name"]
            last_name = user_data["last_name"]
            email = user_data["email"]
            user.first_name = first_name
            user.last_name = last_name
            user.email = email

            db.session.commit()
            self.response["status"] = 200
            self.response["message"] = "User updated successfully"
            return self.response, 200
        else:
            return self.response, 404
api.add_resource(UpdateUser, "/api/update/<int:user_id>")

# Delete request
class DeleteUser(Resource):
    response = {"status": 404, "message": "User not available"}

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            self.response["status"] = 200
            self.response["message"] = "User deleted successfully"
            return self.response, 200

        else:
            return self.response, 404

api.add_resource(DeleteUser, "/api/delete/<int:user_id>")





















if __name__ == '__main__':
    app.run(debug=True)