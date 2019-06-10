import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body></html>'
    page += generator.generate_buzz()
    page += '<br /><h1>Hello from the other side</h1>'
    page += '<h1></body></html>'
    page += '<p> christine</p>'
    return page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))