
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "86f10bc259f1ebeaef9f260b13cc9c86"
@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if str(data.get("cod")) == "200":

                weather = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }

            else:
                error = "City not found!"

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)