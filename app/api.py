import uuid

from flask import jsonify, request, session, redirect, Blueprint
from passlib.hash import pbkdf2_sha256

from app.depends import db

api_router = Blueprint('/', __name__)


class APISessionWorker:

    @staticmethod
    def start_session(user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email Address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    @staticmethod
    def signout():
        session.clear()
        return redirect('/')

    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'),
                                         user['password']):
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401


@api_router.route('/signup', methods=['POST'])
def signup():
    return APISessionWorker().signup()


@api_router.route('/signout')
def signout():
    return APISessionWorker().signout()


@api_router.route('/login', methods=['POST'])
def login():
    return APISessionWorker().login()
