from flask import Flask


app = Flask(__name__)



@app.route("/info")
def lw():
    return "Welcome ALL....Good Morning"


app.run(host='0.0.0.0')





