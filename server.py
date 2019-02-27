from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'T4i5_1s_177y_k34'
print(app.config)
mysql = connectToMySQL('top_deals', app.config['DB_HOST'], app.config['DB_USER'], app.config['DB_PASS'])

@app.route('/')
def index():
    zz = datetime.now()
    query = "SELECT * FROM deals limit 1300"
    x = mysql.query_db(query)

    for passnum in range(len(x)-1,0,-1):
        for i in range(passnum):
            print(x[i]['votes'])
            if x[i]['votes']>x[i+1]['votes']:
                x[i], x[i+1] = x[i+1], x[i]
    newArr = []
    while(len(x)>3):
        for g in range(len(x)-1):
            x[g] = x[g+1]
        x.pop()
    for i in x:
        newArr.append(i['votes'])  

    print("THIS QUERY TOOK:")
    print(datetime.now() - zz, " seconds to process")

    return render_template('index.html', top3 = x)

@app.route('/register')
def create(): 
    for i in range(5000):
        query = 'INSERT INTO deals (name, price, description, vendor_id, created_at, updated_at, votes) VALUES (%(name)s, %(price)s, %(description)s, %(vendor_id)s,NOW(), NOW(), %(votes)s);'
        data = {
            'name': "glasses - "+ str(i),
            'price': 6.99,
            'description': "this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description this is the description ",
            'vendor_id': 5,
            'votes': i
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/logout')
def delete():
    print("delete session",session)
    session.clear()
    print("after delete session",session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)