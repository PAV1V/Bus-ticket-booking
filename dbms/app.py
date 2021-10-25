from flask import Flask, render_template, request, redirect
import mysql.connector
import random

app = Flask(__name__)

def allbus(to_, from_):

    mycursor = mydb.cursor()
    sql = "SELECT * FROM bus WHERE to_ = " + "'" + str(to_) + "'" + " AND from_ = " + "'" + from_ + "'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    return myresult

def busdeatils(busid):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM bus WHERE busid = " + "'" + str(busid) + "'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    return myresult


@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method=="POST":
        from12 = request.form['from']
        to12 = request.form['to']
        return redirect(f"/search/{from12}/{to12}")
    return render_template('index.html')

@app.route('/update', methods = ["GET", "POST"])
def update():
    if request.method=="POST":
        id = request.form['id']
    return render_template('update.html')

@app.route('/search/<from12>/<to12>')
def search(from12, to12):
    details = allbus(to12, from12)
    for x in details: print(x)
    return render_template('search.html', det = details)

@app.route('/book/<int:busid>')
def book(busid):
    busd = busdeatils(busid)
    for i in busd: print(i)
    return render_template('book.html', busd = busd)


@app.route('/booked', methods = ["GET", "POST"])
def booked():
    return render_template('booked.html')


if __name__ == '__main__':

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="projectdb"
    )
    
    app.run(debug=True)