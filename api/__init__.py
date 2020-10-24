from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['e-commerce-beta']
users = db['users']
products = db['products']
from api import login
from api import signup
