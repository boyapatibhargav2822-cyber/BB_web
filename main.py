from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def user_info():
    name = request.form.get("name")
    age = request.form.get("age")
    mail = request.form.get("email")
    quote = request.form.get("quote")

    print(f"name: {name}, age: {age}, mail: {mail}, quote: {quote}")

    return "code:200, success"


if __name__ == "__main__":
    app.run(debug=True)