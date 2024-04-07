from flask import Blueprint, jsonify, session,request
from bson import json_util
from auth import login_required,db


store_bp = Blueprint('store',__name__,url_prefix="/store")

@store_bp.route('/save/to-do/', methods=["POST"])
@login_required
def savetodo():
    r = request.form['todo']
    user= session.get("user")
    mail=user['email']
    print(session)
    existing_doc = db.content.find_one({"email": mail})
    if existing_doc:
        existing_doc["todo"].append(r)
        db.content.update_one({"email": mail}, {"$set": existing_doc})
    else:
        doc = {
            'email':mail,
            'todo':[r],
            'task':[]
        }
        db.content.insert_one(doc)
    return jsonify({"email":mail,"task":r})

@store_bp.route('/get/to-do/',methods=["GET"])
@login_required
def gettodo():
    user= session.get("user")
    mail=user['email']
    if db.content.find_one({'email':mail},{'_id':0}):
        res = dict(db.content.find_one({'email':mail},{'_id':0}))
        return jsonify(res)
    return jsonify({"none":0}), 400

@store_bp.route('/rm/to-do',methods=["POST"])
@login_required
def removetodo():
    t = request.form['todo']
    user= session.get("user")
    mail=user['email']
    print(t)
    db.content.update_one(
    {'email':mail },
    { "$pull": { "todo": t } }
    )
    return jsonify({'msg':'removed {t}'})


#task

@store_bp.route('/save/task/', methods=["POST"])
@login_required
def savetask():
    r = request.form['task']
    user= session.get("user")
    mail=user['email']
    existing_doc = db.content.find_one({"email": mail})
    if existing_doc:
        existing_doc["task"].append(r)
        db.content.update_one({"email": mail}, {"$set": existing_doc})
    else:
        doc = {
            'email':mail,
            'todo':[],
            'task':[r]
        }
        db.content.insert_one(doc)
    return jsonify({"email":mail,"task":r})

@store_bp.route('/get/task/',methods=["GET"])
@login_required
def gettask():
    user= session.get("user")
    mail=user['email']
    if db.content.find_one({'email':mail},{'_id':0}):
        res = dict(db.content.find_one({'email':mail},{'_id':0}))
        return jsonify(res)
    return jsonify({"none":0}), 400

@store_bp.route('/rm/task',methods=["POST"])
@login_required
def removetask():
    t = request.form['task']
    user= session.get("user")
    mail=user['email']
    print(t)
    db.content.update_one(
    {'email':mail },
    { "$pull": { "task": t } }
    )
    return jsonify({'msg':'removed {t}'})