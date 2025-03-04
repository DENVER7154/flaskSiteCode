from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/username_test")
def username_test():
    username=request.args.get("username")
    return render_template("usernameTest.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)