from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import connection

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = connection.DB_URI
db = SQLAlchemy(app)