from flask import Flask

from routes import route_bp
from auth import auth_bp
from store import store_bp

app = Flask(__name__)
app.secret_key= b"\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5"

app.register_blueprint(route_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(store_bp)

if __name__ == "__main__":
    app.run(debug=True)