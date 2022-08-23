import math
from flask import Flask, render_template, request, url_for,redirect, session


application = Flask(__name__)
application.secret_key = '3182731731231283'

square = co2 = electricityval = gasval = electricitytree = gastree = total = square_noint = co2_notint = ""


@application.route('/', methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        session["square_noint"] = request.form.get("square")
        session["co2_notint"] = request.form.get("co2")
        session["square"] = float(request.form.get("square"))
        session["co2"] = float(request.form.get("co2"))
        
        return redirect("/goal")
    
    return render_template("index.html", squareval = electricityval, co2val = gasval, usersquare = square_noint, userco2 = co2_notint, electree=electricitytree, gtree =  gastree, total_tree = total)

@application.route("/college/")
def college():
    return render_template("college.html")

@application.route('/goal', methods = ["POST", "GET"])
def goal():
    square_noint = session.get("square_noint")
    co2_notint = session.get("co2_notint")
    square = session.get("square")
    co2 = session.get("co2")
    electricityval = round((10 * square / 1000) * co2,2)
    gasval = round((50 * square / 96.43) * 11.7, 2)
    electricitytree =  math.ceil(electricityval / 2400)
    gastree = math.ceil(gasval / 2400)
    total = electricitytree + gastree
    return render_template("goal.html", squareval = electricityval, co2val = gasval, usersquare = square_noint, userco2 = co2_notint, electree=electricitytree, gtree =  gastree, total_tree = total)


if __name__ == "__main__":
    application.run(debug=True)
    
