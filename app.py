import time
import mysql.connector

from flask import Flask
app = Flask(__name__)

contador = 0



def get_hit_count():
    global contador
    contador = contador +1 
    return contador

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)