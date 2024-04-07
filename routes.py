from flask import Blueprint, request, render_template, redirect
from auth import login_required

route_bp = Blueprint('route',__name__)

@route_bp.route('/')
def root():
    return redirect('/home')

@route_bp.route('/login/')
def loginpage():
    return render_template("login.html")

@route_bp.route('/signup/')
def signuppage():
    return render_template("signup.html")

@route_bp.route('/home/')
@login_required
def home():
    return render_template("index.html")

@route_bp.route('/todolist/')
@login_required
def todopage():
    return render_template('todolist.html')

@route_bp.route('/task/')
@login_required
def taskspage():
    return render_template('tasks.html')