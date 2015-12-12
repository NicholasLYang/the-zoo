from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template("index.html")
    else:
        if session.get('user') == None:
            return render_template("login.html")
        else:
            return render_template("index.html")
    return render_template("login.html")

@app.route("/community/<community>", methods=["GET", "POST"]))
def communities(community):
    if request.method == "POST":
        code = request.form["code"]
        return render_template("community.html")
    return render_template("community.html")

@app.route("/user/<user>")
def user(user):
    return render_template("user.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/creategroup")
def creategroup():
    return render_template("/creategroup.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
