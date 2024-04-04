from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static/'

with open('model.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
   return render_template('Home.html')
@app.route('/about')
def about():
    return render_template('GoldR.html')
@app.route("/index")
def index():
    return render_template("data.html")
@app.route("/display" , methods=['GET', 'POST'])
def display():
    if request.method=='POST':
        date = request.form['date']
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        c_date = pd.Timestamp(year=year, month=month, day=day)
        day_of_year = c_date.dayofyear
        # Predict the gold price for the input date
        predicted_price = model.predict([[day_of_year]])
        r_number = (round(predicted_price[0], 2) - 51) * 83.3
        rounded_number = round(r_number,2)
        return render_template("display.html", data=rounded_number)
if __name__ =='__main__':
   app.run(debug=True)
