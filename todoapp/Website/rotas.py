from flask import Flask, Blueprint, render_template

page = Flask(__name__)

@page.route('/')
def home():
    return render_template ("index.html")