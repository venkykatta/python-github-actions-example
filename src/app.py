from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello CI/CD"

if __name__ == "__main__":
    app.run()
