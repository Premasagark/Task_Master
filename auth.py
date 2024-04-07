from flask import Blueprint, session, jsonify,redirect,request
from passlib.hash import pbkdf2_sha256
import uuid
from functools import wraps
from pymongo import MongoClient

auth_bp = Blueprint('auth',__name__,url_prefix='/user')

client = MongoClient("mongodb+srv://Premasagar:mongodb25@sparta.zdlbuvp.mongodb.net/")
db = client.task_db

#functions
def login_required(f):
  
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/login')
  
  return wrap

def start_session(user):
    del user['pwd']
    del user['_id']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user,{'msg':"Success"}) 



@auth_bp.route("/signup/", methods=["POST"] )
def create_acc():
#    us= User()
#    return us.signup()
    name = request.form["name"]
    email = request.form["email"]
    pwd = request.form["pwd"]
    pwd = pbkdf2_sha256.encrypt(pwd)
    print(name, email, pwd)
    
    if db.users.find_one({ "email": email}):
      return jsonify({ "msg": "Email address already in use" })
    # res = db.users.find({"email":email})
    # doc = {"msg": "Signup successfully completed!"}
    # print(res)
    db.users.insert_one(
        {
            "_id": uuid.uuid4().hex,
            "user_name": name,
            "email":email,
            "pwd":pwd
        }
    )
    return jsonify({"msg": "Signup successfully completed!"}), 200

@auth_bp.route("/login/", methods=["POST"])
def chk_login():
   user = db.users.find_one({
      "email": request.form['email']
    })
   if user and pbkdf2_sha256.verify(request.form['pwd'], user['pwd']):
        return start_session(user), 200
   return jsonify({ "msg": "Invalid login credentials" }), 400

@auth_bp.route("/signout/")
def signout():
   session.clear()
   return redirect("/login")