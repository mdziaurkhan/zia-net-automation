#check this document for initial/minimal config: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# to use templates we have to import render_template
from flask import Flask, render_template
app = Flask(__name__)   # we creared this variable name "app"

iso_switches = ['zia-R1','zia-R3','zia-R3','zia-R4']
#switch = 0

@app.route('/')             # / is the root page of our webpage
@app.route('/home')             # / is the root page of our webpage
def home():
    return render_template('home.html', zia_ios_switches = iso_switches)  # using home.html under template folder

@app.route('/resources')
def Resources():  # for multiline use """
    return render_template('resources.html', title = 'resources') # using resources.html under template folder



#to avoid "flusk run" command and run the webpage with "python zia-flask-1.py"
if __name__ == '__main__':
    app.run(debug = True)
