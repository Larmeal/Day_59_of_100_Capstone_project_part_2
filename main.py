from flask import Flask, render_template
import requests

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
content = response.json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", contents=content)

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/Contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    port_number = content[id - 1]
    return render_template("post.html", articles=port_number)



if __name__ == "__main__":
    app.run(debug=True)