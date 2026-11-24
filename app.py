from flask import Flask

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return "<h1>Merhaba, Python ile ilk web sitem!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
