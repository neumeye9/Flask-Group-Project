from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('option1.html')

@app.route('/left')
def firstleft():
    print "First left page"
    return render_template('option2left.html')

@app.route('/right')
def firstright():
    return render_template('option2right.html')

@app.route('/right/nextleft')
def nextleft():
    return render_template('option3left.html')

@app.route('/right/nextright')
def nextright():
    return render_template('option3right.html')

app.run(host='192.168.1.62.',port=5000,debug=True)

