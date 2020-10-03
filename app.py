import mysql.connector

from flask import Flask
app = Flask(__name__)

data = '-'



@app.route('/')
def hello():
    mydb = mysql.connector.connect(host='172.18.0.3',port='3306',user='root',password='root',database='sa_db',auth_plugin='mysql_native_password')    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM usuario')
    myresult = mycursor.fetchall()
    data = ''
    for x in myresult:
        #print(x)
        data = data + '\n\n' + str(x)
        #print(mydb)
    return 'Contenido de la base de datos {} \n'.format(data)