from flask import Flask
def create_app(testing:bool=True):
 app = Flask(__name__)

 @app.route("/")
 def index():
   return "Hello world <br> Testing:(testing)"
 return app