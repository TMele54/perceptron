from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    user = 'Tony Mele'
    return render_template("index.html", name=user)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
