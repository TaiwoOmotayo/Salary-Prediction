from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("salary_prediction.sav", "rb"))

# Mapping functions
def map_sex(sex):
    return {'F': 0, 'M': 1}.get(sex, -1)

def map_designation(designation):
    return {'Analyst': 0, 'Associate': 1, 'Director': 2, 'Manager': 3, 'Senior Analyst': 4, 'Senior Manager': 5}.get(designation, -1)

def map_unit(unit):
    return {'Finance': 0, 'IT': 1, 'Management': 2, 'Marketing': 3, 'Operations': 4, 'Web': 5}.get(unit, -1)

def map_leaves_used(leaves_used):
    return {15.0: 0, 16.0: 1, 17.0: 2, 18.0: 3, 19.0: 4, 20.0: 5, 21.0: 6, 22.0: 7, 23.0: 8, 24.0: 9,
            25.0: 10, 26.0: 11, 27.0: 12, 28.0: 13, 29.0: 14, 30.0: 15}.get(leaves_used, -1)

def map_ratings(ratings):
    return {2.0: 0, 3.0: 1, 4.0: 2, 5.0: 3}.get(ratings, -1)

def map_year_joined(year):
    return {2009: 0, 2010: 1, 2011: 2, 2012: 3, 2013: 4, 2014: 5, 2015: 6}.get(year, -1)

def map_month_joined(month):
    return {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11}.get(month, -1)

def map_day_joined(day):
    return {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11,
            13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21,
            23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30}.get(day, -1)

def map_dayofweek_joined(dayofweek):
    return {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}.get(dayofweek, -1)

# Display Homepage
@app.route("/")
def home():
    result = ""
    return render_template("index.html", result=result)

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:
            SEX = map_sex(request.form["SEX"])
            DESIGNATION = map_designation(request.form["DESIGNATION"])
            AGE = float(request.form["AGE"])
            UNIT = map_unit(request.form["UNIT"])
            LEAVES_USED = map_leaves_used(float(request.form["LEAVES USED"]))
            RATINGS = map_ratings(float(request.form["RATINGS"]))
            YEAR_JOINED = map_year_joined(int(request.form["year joined"]))
            MONTH_JOINED = map_month_joined(int(request.form["month joined"]))
            DAY_JOINED = map_day_joined(int(request.form["day joined"]))
            DAYOFWEEK_JOINED = map_dayofweek_joined(int(request.form["dayofweek joined"]))

            # Predict using the model
            result = model.predict([[SEX, DESIGNATION, AGE, UNIT, LEAVES_USED, RATINGS,
                                     YEAR_JOINED, MONTH_JOINED, DAY_JOINED, DAYOFWEEK_JOINED]])[0]
        except Exception as e:
            result = f"Error: {str(e)}"
    else:
        result = ""
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
