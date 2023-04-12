from flask import Flask, render_template, flash,redirect, url_for, request
from flask_mysqldb import MySQL
import sqlite3 as sql
import pymysql



def sql_connector():
    conn = pymysql.connect(user="root", password="", db="flask",host="localhost")
    c = conn.cursor()
    return conn,c


app = Flask(__name__, static_url_path='/static')
app.secret_key = "my_secret_key"


app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= ""
app.config["MYSQL_DB"]= "flask"

mysql = MySQL(app)


present_user = []



@app.route("/")
def home():
    return render_template('main_base.html')


@app.route("/wrong_password")
def wrong_password_email():
    return render_template('wrong_password_email.html')




#Education
@app.route("/Welcome_Education")
def children_signin_submit():
    return render_template("children_welcome.html")


@app.route("/children_login", methods=["GET", "POST"])
def children_login():
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        
        conn, c = sql_connector()
        c.execute("insert into edu_details values('{}','{}')".format(Email, password))
        conn.commit()
        conn.close()
        c.close()
    return render_template("children_login.html")

@app.route("/children_signup", methods=["GET", "POST"])
def children_signup():
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        conn, c = sql_connector()
        c.execute("insert into edu_signup_details values('{}','{}')".format(Email, password))
        conn.commit()
        conn.close()
        c.close()
    return render_template("children_signup.html")

@app.route("/children_request", methods=["GET", "POST"])
def children_request():
    if request.method== "POST":
        Name = request.form.get("NGO_name")
        Email= request.form.get("email")
        Phone = request.form.get("phone")
        Address = request.form.get("address")
        NGO_registration_ID = request.form.get("NGO_registration_ID")
        Amount = request.form.get("amount")
        conn, c = sql_connector()
        c.execute("insert into children_details(NGO_Name, Email, Phone, City, NGO_registration_ID,Amount) values('{}','{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,NGO_registration_ID,Amount))
        conn.commit()
        conn.close()
        c.close()
    return render_template("children_request.html")

@app.route("/education_request_sent")
def education_request_sent():
    return render_template("education_request_sent.html")


@app.route('/children_pending_request')
def children_pending_request():
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT NGO_Name,email,status FROM children_details where NGO_Name="SS"')
    rows = cur.fetchall()
    cur.close()
    return render_template('children_pending_request.html',rows=rows)





#FARMERS
@app.route("/Welcome_farmer")
def farmer_signin_submit():
    return render_template("farmer_welcome_page.html")



def check_user(email, password):
    conn, c = sql_connector()
    
    c.execute("SELECT * FROM farmer_signup_details WHERE Username=%s AND password=%s", (email, password))
    result = c.fetchone()
    conn.commit()
    conn.close()
    c.close()
    if result:
        present_user = email
        return True
    else:
        return False
    
    
    


@app.route("/farmers", methods=["GET", "POST"])
def farmers():
    if request.method == "POST":
        global email
        email = request.form.get("email")
        password = request.form.get("password")
        if check_user(email, password):
            return render_template('farmer_welcome_page.html')
        else:
            # flash('Wrong Username/Password')
            # return render_template('farmer.html')
            return render_template("wrong_password_email.html")
    else:
        return render_template('farmer.html')


        

@app.route("/farmers_signup", methods=["GET", "POST"])
def farmers_signup():
    a = False
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        conn, c = sql_connector()
        c.execute("insert into farmer_signup_details values('{}','{}')".format(Email, password))
        conn.commit()
        conn.close()
        c.close()
        a = True
    if a == True:
        return render_template('redirecting_page.html')
    return render_template("farmer_signup.html")

@app.route("/farmer_request", methods=["GET", "POST"])
def farmer_request():
    if request.method== "POST":
        Name = request.form.get("name")
        Email= request.form.get("email")
        Phone = request.form.get("phone")
        Address = request.form.get("address")
        Farmer_ID = request.form.get("Farmer_ID")
        conn, c = sql_connector()
        c.execute("insert into farmer_details (Name,Email,Phone,Address,Farmer_ID) values('{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,Farmer_ID))
        conn.commit()
        conn.close()
        c.close()
    return render_template("farmer_request.html")

@app.route("/farmer_request_sent")
def farmer_request_sent():
    return render_template("farmer_request_sent.html")


@app.route('/pending_request')
def farmer_pending_request():
    # conn, c = sql_connector()

    
    cur = mysql.connection.cursor()
    cur.execute("SELECT name,email,status FROM farmer_details where name='tia'")
    # c.execute("SELECT * FROM farmer_signup_details WHERE Username=%s AND password=%s", (email, password))

    rows = cur.fetchall()
    cur.close()
    return render_template('farmer_pending_request.html',rows=rows)


@app.route('/post-data-url', methods=['POST'])
def post_data():
    # Handle the data post
    
    if request.method== "POST":
        Name = request.form.get("name")
        Email= request.form.get("email")
        Phone = request.form.get("phone")
        Address = request.form.get("address")
        Farmer_ID = request.form.get("Farmer_ID")
        conn, c = sql_connector()
        c.execute("insert into farmer_details values('{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,Farmer_ID))
        conn.commit()
        conn.close()
        c.close()
    return {"status": "success"}, 200

#not using for now
@app.route('/other-page')
def other_page_route():
    return render_template('other-page.html')

@app.route('/redirect')
def redirect_page():
    return render_template('redirecting_page.html')







if __name__ == '__main__':
    
    app.run(host = "localhost",port=8000, debug=True)
    
    

    
    
    
# def add_data(Email,password):
#     try:
#         con = sql.connect('flask_database.db')
#         # Getting cursor
#         c =  con.cursor() 
#         # Adding data
#         c.execute("INSERT INTO details (Username, Password) VALUES (%s, %s)" %(Email, password))
        
#         # Applying changes
#         con.commit() 
#     except:
#         print("An error has occured")



# def home():
#     cur = mysql.connection.cursor()
#     cur.execute("Select * from details")
#     fetchdata = cur.fetchall()
#     cur.close()
#     return render_template("abc.html", data = fetchdata)