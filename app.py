from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_homepage():
    return render_template("index.html")


@app.route('/<string:page_name>')
def my_served_page(page_name):
    return render_template(f"{page_name}")
