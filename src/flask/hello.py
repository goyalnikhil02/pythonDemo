from flask import Flask
app = Flask(__name__)
@app.route("/hello") 
@app.route("/")
def hello():
    return "Hello World!"
 
@app.route("/user")
def helloUser():
    return "Hello user"

@app.route("/member")
def helloMember():
    return "Hello members"

@app.route("/members/<string:name>")
def getMembers(name):
    return "Hi"+" : "+name


if __name__ == "__main__":
    app.run()