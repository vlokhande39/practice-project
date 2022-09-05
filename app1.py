from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('modellll.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        undergrad = request.form['Undergrad']
        if undergrad == 'YES':
            undergrad = 1
        else:
            undergrad = 0
        marital_status = request.form['Marital.Status']
        if marital_status == "Divorced":
            marital_status = 0
        elif marital_status == "Married":
            marital_status = 1
        else:
            marital_status = 2
        urban = request.form["Urban"]
        if urban == "Yes":
            urban = 1
        else:
            urban = 0
        city_population = int(request.form['City.Population'])
        work_experience = int(request.form['Work.Experience'])
        
        prediction = model.predict([[undergrad, marital_status, city_population, work_experience, urban]])
        #  output=prediction
        if prediction == 1:
            return render_template('home.html', prediction_text="risky")
        else:
            return render_template('home.html', prediction_text="good")
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
