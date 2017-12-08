from flask import Flask,jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./cars.json').read())
data=jData["CarModels"]

@app.route('/')
def car_main():
    return render_template("index.html")

@app.route('/getcars/')
def car_all():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getcars/<string:Type>/')
def car(Type=''):
    myList=[]
    for element in data:
        if element["Type"] == Type:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
