from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open(r'C:\Users\Siddhi Sankhe\Desktop\Compozent Task\ML_Project\ML_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        data = request.form
        open_price = float(data.get("open"))
        close_price = float(data.get("close"))
        volume = float(data.get("volume"))
        year = int(data.get("year"))
        month = int(data.get("month"))
        day_of_the_week = int(data.get("day_of_the_week"))
        average_price = float(data.get("Average_price"))
        price_range = float(data.get("Price_Range"))

        # Create input array for the model
        user_input = np.array([[open_price, close_price, volume, year, month, day_of_the_week, average_price, price_range]])
        model_output = model.predict(user_input)

        # Render prediction result on the same page
        return render_template('index.html', prediction=f"Predicted Close Price: {model_output[0]:.2f}")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
