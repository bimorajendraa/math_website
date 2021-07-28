from flask import Flask, render_template,request

from formula import bangundatar

oop = bangundatar()

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/pyshics")
def pyshics():
    return render_template("pyshics.html")

@app.route("/square")
def square():
    return render_template("square.html")

@app.route("/send", methods=['POST'])
def send():
    if request.method == 'POST':
        num = request.form['num']
        num = float(num)
        shape = oop.persegi(num)
        total = shape.keliling()
        return render_template("square.html", total=total)

if __name__ == '__main__':
    app.run(debug=True)