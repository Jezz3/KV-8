from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/Luftfeuchtigkeit")
def index2():
    return render_template("index2.html")

@app.route("/Luftdruck")
def index3():
    return render_template("index3.html")

if __name__ == '__main__':

 app.run(debug=True, host='0.0.0.0')
