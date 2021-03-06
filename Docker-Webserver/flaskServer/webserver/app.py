from flask import Flask, render_template
import mariadb

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "This is the login page"

@app.route('/database', methods=['GET', 'POST'])
def database():
    config = {'host': '<IP_Address_of_MySql_container>','port': 3306,'user': 'me','password': 'yourSAFEpassword','database': 'student'}
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    sql= "SELECT * FROM student"
    cur.execute (sql)
    myresult = cur.fetchall()
    return "{}".format(myresult)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
