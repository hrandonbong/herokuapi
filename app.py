from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)

@app.route("/prices", methods=["POST"])
def prices():
    if request.form:
        input = request.form
    else:
        input = request.json
    item = input["items"]
    url = "https://www.google.com/search?q=" + item + "&tbm=shop"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find("span",{"class":"HRLxBb"})
    return price.text, 200,{'Content-Type': 'text/plain'}

if __name__== '__main__':
    app.run(debug=True)
