from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the home of the page with DEBUG on."