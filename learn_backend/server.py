from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Forecast'
    weather_text = weather_by_city('Yekateringburg,Russia')

    return render_template('index.html', page_title=title, weather=weather_text)

if __name__ == '__main__':
    app.run(debug=True)
