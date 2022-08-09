import math
from flask import Flask, render_template,request,url_for
from numpy import require

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
    square = ""
    co2 = ""
    electricityval = "" 
    gasval = ""
    electricitytree = ""
    gastree = ""
    unround_electricityval = ""
    unround_gasval = ""
    total = ""
    square_noint = ""
    co2_notint = ""
    if request.method == "POST":
        square_noint = request.form.get("square")
        co2_notint = request.form.get("co2")
        square = int(request.form.get("square"))
        co2 = int(request.form.get("co2"))
        electricityval = round((10 * square / 1000) * co2,2)
        unround_electricityval = (10 * square / 1000) * co2
        gasval = round((50 * square / 96.43) * 11.7, 2)
        electricitytree =  math.ceil(electricityval / 2400)
        gastree = math.ceil(gasval / 2400)
        total = electricitytree + gastree

    
    return render_template("index.html", squareval = electricityval, co2val = gasval, usersquare = square_noint, userco2 = co2_notint, electree=electricitytree, gtree =  gastree, total_tree = total)
    

if __name__ == "__main__":
    app.run(debug=True)
    