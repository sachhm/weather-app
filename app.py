from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def index():
    todays_weather = "TODAY'S WEATHER GO BRRRRRRR"
    week_forecast = "Work in progress"
    return render_template('index.html', todays_weather=todays_weather, week_forecast=week_forecast)

@app.route('/about')
def about():
    author = "Sachh Moka"
    return render_template('about.html',author=author)
    
if __name__ == '__main__':
    app.run()   