# import weather, location
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index():
    # location_data = location.get_location()
    # city = location_data["city"]
    # country = location_data["country"]
    # max_temp = round(weather.get_maximum_temperature(),2)
    # min_temp = round(weather.get_minimum_temperature(),2)

    # dummy input
    city = "City"
    country = "Country"
    max_temp = 2.31
    min_temp = -10.31
    
    return render_template('index.html', city=city, country=country, max_temp=max_temp, min_temp=min_temp)

@app.route('/about')
def about():
    author = "Sachh Moka"
    return render_template('about.html',author=author)
    
if __name__ == '__main__':
    app.run()   