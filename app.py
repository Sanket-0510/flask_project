from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'title': 'frontend',
    'location': 'mumbai',
    'salary': 100000
},{
     'title': 'backend',
    'location': 'bangloru',
    'salary': 200000
},{
     'title': 'full stack',
    'location': 'kalyan',
    'salary': 300000
}]
@app.route("/")
def run():
    return render_template('home.html', jobs=JOBS)


