from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def index():
    location = location.get_ip()
    return render_template('index.html')

@app.route('/about')
def about():
    author = "Sachh Moka"
    return render_template('about.html',author=author)
    
if __name__ == '__main__':
    app.run()   