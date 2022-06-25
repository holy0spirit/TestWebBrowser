from flask import Flask, request, jsonify
import webbrowser

app = Flask(__name__)


@app.route('/', methods=['GET'])
def testBrowser():
    new = 2
    url = 'index.html'

    webbrowser.open(url,new)

    return '200'

