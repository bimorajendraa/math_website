from flask import Flask, render_template,request
from formula import bangundatar

oop = bangundatar()

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/math")
def math_home():
    return render_template("math_home.html")

@app.route("/send", methods=['POST'])
def formula():
    if request.method == 'POST':
        if request.form["key"] == "keliling":
            number = request.form["sisi"]
            number = float(number)
            shape = oop.persegi(number)
            total = shape.keliling()
            return render_template("square.html", total=total)
        elif request.form["key"] == "luas":
            number = request.form["sisib"]
            number = float(number)
            shape = oop.persegi(number)
            total = shape.luas()
            return render_template("square.html", total=total)
        elif request.form["key"] == "diagonal":
            total = 13 + 20
            return render_template("square.html", total=total)

            



if __name__ == '__main__':
    app.run(debug=True)