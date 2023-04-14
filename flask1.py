from flask import Flask, render_template, flash,redirect, url_for, request
from flask_mysqldb import MySQL
import sqlite3 as sql
import pymysql
from bs4 import BeautifulSoup
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


current_user = []

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




#Education
@app.route("/Welcome_Education")
def children_signin_submit():
    return render_template("children_welcome.html")





@app.route("/children_signup", methods=["GET", "POST"])
def children_signup():
    a = False
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        user_name = request.form.get("user_name")
        conn, c = sql_connector()
        c.execute("insert into NGO_signup_details values('{}','{}','{}')".format(Email, password,user_name))
        conn.commit()
        conn.close()
        c.close()
        a = True
    if a == True:
        return render_template('children_redirecting_page.html')
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
        c.execute("insert into NGO_request_details(NGO_Name, Email, Phone, City, NGO_registration_ID,Amount) values('{}','{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,NGO_registration_ID,Amount))
        conn.commit()
        conn.close()
        c.close()
    return render_template("children_request.html")

@app.route("/education_request_sent")
def education_request_sent():
    return render_template("education_request_sent.html")



    



children_email = ""
@app.route("/children_login", methods=["GET", "POST"])
def children_login():
    global children_email
    if request.method == "POST":
        children_email = request.form.get("email")
        password = request.form.get("password")
        if children_check_user(children_email, password):
            return render_template('children_welcome.html')
        else:
            return render_template("children_wrong_password_email.html")
    else:
        return render_template('children_login.html')




    
@app.route('/children_pending_request')
def children_pending_request():
    global children_email
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT NGO_Name,email,status FROM NGO_request_details  where email=%s", (children_email,))
    
    rows = cur.fetchall()
    cur.close()
    return render_template('children_pending_request.html',rows=rows)
    # return children_email



def children_check_user(email, password):
    conn, c = sql_connector()
    
    c.execute("SELECT * FROM NGO_signup_details WHERE Username=%s AND password=%s", (email, password))
    result = c.fetchone()
    conn.commit()
    conn.close()
    c.close()
    if result:
        present_user = email
        return True
    else:
        return False
    




#FARMERS
@app.route("/Welcome_farmer")
def farmer_signin_submit():
    return render_template("farmer_welcome_page.html")



def farmer_check_user(email, password):
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
        global farmer_email
        
        farmer_email = request.form.get("email")
        password = request.form.get("password")

        
        if farmer_check_user(farmer_email, password):
            return render_template('farmer_welcome_page.html')
        else:
          
            return render_template("farmer_wrong_password_email.html")
    else:
        return render_template('farmer.html')



        

@app.route("/farmers_signup", methods=["GET", "POST"])
def farmers_signup():
    a = False
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        user_name = request.form.get("user_name")
        conn, c = sql_connector()
        c.execute("insert into farmer_signup_details values('{}','{}','{}')".format(Email, password,user_name))
        conn.commit()
        conn.close()
        c.close()
        a = True
    if a == True:
        return render_template('farmers_redirecting_page.html')
    return render_template("farmer_signup.html")



@app.route("/farmer_request", methods=["GET", "POST"])
def farmer_request():
    if request.method== "POST":
        Name = request.form.get("name")
        Email= request.form.get("email")
        Phone = request.form.get("phone")
        Address = request.form.get("address")
        Farmer_ID = request.form.get("Farmer_ID")
        Age = request.form.get("age")
        Amount = request.form.get("amount") 
        conn, c = sql_connector()
        c.execute("insert into farmer_details (Name,Email,Phone,Address,Farmer_ID,age,amount) values('{}','{}','{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,Farmer_ID,Age,Amount))
        conn.commit()
        conn.close()
        c.close()
    return render_template("farmer_request.html")
    

@app.route("/farmer_request_sent")
def farmer_request_sent():
    return render_template("farmer_request_sent.html")

    

 

 

 
 
 
@app.route('/farmer_pending_request')
def farmer_pending_request():
    global farmer_email
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT name,email,status FROM farmer_details where email=%s", (farmer_email,))
    
    

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




@app.route('/admin')
def admin():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT count(*) FROM farmer_details ")
    # cur.execute("SELECT 'Farmers' as type, COUNT(*) as count FROM farmer_details UNION SELECT 'NGO' as type, COUNT(*) as count FROM farmer_signup_details UNION SELECT 'Donors' as type, COUNT(*) as count FROM edu_details;")

    # f_details = cur.fetchall()
    f_details= cur.fetchone()
    cur.execute("SELECT count(*) FROM NGO_request_details ")
    e_details = cur.fetchone()
    cur.execute("SELECT count(*) FROM NGO_signup_details ")
    e_signup_details = cur.fetchone()
    cur.execute("SELECT count(*) FROM farmer_signup_details ")
    f_signup_details = cur.fetchone()
    
    
    cur.execute("select sum(amount) from farmer_details")
    f_sum = cur.fetchone()

    cur.execute("select sum(amount) from NGO_request_details")
    e_sum = cur.fetchone()
    
    cur.execute("SELECT sum(amount) FROM donors ")
    total_Amount_donated = cur.fetchall()
    
    cur.close()
    
    total_Amount_donated=str(total_Amount_donated)
            
    total_Amount_donated = total_Amount_donated.replace('(', '').replace(')', '').replace(',', '').replace('Decimal', '').replace("'", "")

    total_Amount_donated = int(total_Amount_donated)
    
    
    f_sum=str(f_sum)
            
    f_sum = f_sum.replace('(', '').replace(')', '').replace(',', '').replace('Decimal', '').replace("'", "")

    f_sum = int(f_sum)
    
   
    e_sum=str(e_sum)
            
    e_sum = e_sum.replace('(', '').replace(')', '').replace(',', '').replace('Decimal', '').replace("'", "")

    e_sum = int(e_sum)
    
    f_details=str(f_details)
            
    f_details = f_details.replace('(', '').replace(')', '').replace(',', '')

    f_details=int(f_details)
    
    e_details=str(e_details)
            
    e_details = e_details.replace('(', '').replace(')', '').replace(',', '')

    e_details=int(e_details)
    
    e_signup_details=str(e_signup_details)
            
    e_signup_details = e_signup_details.replace('(', '').replace(')', '').replace(',', '')

    e_signup_details=int(e_signup_details)
    
    f_signup_details=str(f_signup_details)
            
    f_signup_details = f_signup_details.replace('(', '').replace(')', '').replace(',', '')

    f_signup_details=int(f_signup_details)
    
    
    total_users = e_signup_details + f_signup_details
    
    farmer_total_requested_amount = f_sum
    NGO_total_requested_amount = e_sum

    total_amount_requested = farmer_total_requested_amount+NGO_total_requested_amount
    
    return render_template("admin.html",data=f_details,data2 = e_details,data3 = e_signup_details,data4 = f_signup_details,total = total_users,farmer_total = farmer_total_requested_amount,NGO_total = NGO_total_requested_amount,total_amount_requested=total_amount_requested,total_Amount_donated = total_Amount_donated)
    
    # return total_users



@app.route('/admin_users')
def admin_users():
    
    return render_template("admin_users.html")

@app.route('/admin/login',methods = ["GET", "POST"])
def admin_login():
    if request.method == "POST":
        admin_id = request.form.get("admin_id")
        password = request.form.get("password")
        if admin_check_user(admin_id, password):
            return render_template('admin_redirect_homepage.html')
        else:
            return render_template("admin_wrong_password_email.html")
    else:
        return render_template('admin_login.html')

def admin_check_user(admin_id, password):
    conn, c = sql_connector()
    
    c.execute("SELECT * FROM admin WHERE id=%s AND password=%s", (admin_id, password))
    result = c.fetchone()
    conn.commit()
    conn.close()
    c.close()
    if result:

        return True
    else:
        return False
    
@app.route('/admin/wrong/input')
def admin_wrong_password_email():
    
    return render_template("admin_wrong_password_email.html")

@app.route('/admin_users/farmers')
def admin_user_farmer():
    
    cur = mysql.connection.cursor()
   
    
    cur.execute("SELECT Name, Email, Phone, Address, Farmer_ID, Status,Age,amount FROM farmer_details ")
    details = cur.fetchall()
  
    return render_template("admin_farmer_option.html",details=details)
    # return details

@app.route('/admin_users/farmers/update/<string:SL_No>', methods=['POST'])
def update_farmer_status(SL_No):
    sno = SL_No
    status = request.form['status']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE farmer_details SET Status = %s WHERE name = %s", (status, sno))
    mysql.connection.commit()
    cur.close()
    
    flash('Status updated successfully!', 'success')
    # return sno
    return redirect(url_for('admin_user_farmer'))

@app.route('/admin_users/NGO')
def admin_user_NGO():
    cur = mysql.connection.cursor()
   
    
    cur.execute("SELECT ID, NGO_NAME, Email, Phone, City, NGO_REGISTRATION_ID,AMOUNT,status FROM NGO_request_details ")
    details = cur.fetchall()
  
    return render_template("admin_NGO_option.html",details=details)
    # return details
    # return render_template("admin_NGO_option.html")


@app.route('/admin_users/NGO/update/<string:SL_No>', methods=['POST'])
def update_NGO_status(SL_No):
    sno = SL_No
    status = request.form['status']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE NGO_request_details SET Status = %s WHERE id = %s", (status, sno))
    mysql.connection.commit()
    cur.close()
    
    flash('Status updated successfully!', 'success')
    # return sno
    
    return redirect(url_for('admin_user_NGO'))


@app.route('/admin_users/donors')
def admin_user_donors():
    cur = mysql.connection.cursor()
   
    
    cur.execute("SELECT * FROM donors ")
    details = cur.fetchall()
  
    return render_template("admin_donors_option.html",details=details)


#DONORS
@app.route('/donors/signup', methods=["GET", "POST"])
def donors_signup():
    a = False
    if request.method== "POST":
        Email= request.form.get("email")
        password = request.form.get("password")
        user_name = request.form.get("user_name")
        conn, c = sql_connector()
        c.execute("insert into donor_signup_details values('{}','{}','{}')".format(Email, password,user_name))
        conn.commit()
        conn.close()
        c.close()
        a = True
    if a == True:
        return render_template('donors_redirecting_page.html')
    return render_template("donors_signup.html")



donors_email = ""    
@app.route('/donors/login', methods=["GET", "POST"])
def donors_login():
    global donors_email
    if request.method == "POST":
        donors_email = request.form.get("email")
        password = request.form.get("password")
        if donors_check_user(donors_email, password):
            return render_template('donors_welcome.html')
        else:
            return render_template("donors_wrong_password_email.html")
    else:
        return render_template('donors_login.html')


def donors_check_user(email, password):
    conn, c = sql_connector()
    
    c.execute("SELECT * FROM donor_signup_details WHERE Username=%s AND password=%s", (email, password))
    result = c.fetchone()
    conn.commit()
    conn.close()
    c.close()
    if result:
        present_user = email
        return True
    else:
        return False
    
@app.route('/donors/welcome')
def donors_welcome():
    return render_template("donors_welcome.html")

@app.route('/donors/mydonation', methods=["GET", "POST"])
def donors_mydonation():
    global donors_email
    # cur = mysql.connection.cursor()

    if request.method== "POST":
        
        Name= request.form.get("Name")
        
        conn, c = sql_connector()
        
        c.execute("SELECT * FROM donors where first_name = '{}' ".format(Name))
        conn.commit()
        conn.close()
        c.close()
        
        details = c.fetchall()
  
        return render_template("donors_mydonation.html",details=details)
    return render_template("donors_mydonation.html")


   
@app.route("/donors/donate", methods=["GET", "POST"])
def donors_donate():
    a = False
    if request.method== "POST":
        first_name= request.form.get("firstName")
        last_name= request.form.get("lastName")
        amount = request.form.get("amount")
        conn, c = sql_connector()
        c.execute("insert into donors values('{}','{}','{}')".format(first_name,last_name,amount))
        conn.commit()
        conn.close()
        c.close()
        a = True
    if a == True:
        return render_template('donors_donate_redirecting_page.html')
        # return amount
    return render_template("donors_donate.html")


@app.route("/donors_track")
def donors_track():
    return render_template("donors_track.html")

@app.route("/donors_card_details")
def donors_card_details():
    return render_template("donors_card_details.html")

@app.route("/donors/redirecting")
def donors_redirecting():
    return render_template("donors_redirecting.html")

@app.route("/donors/thankyou")
def donors_thankyou():
    return render_template("donors_thankyou.html")

if __name__ == '__main__':
    
    app.run(host = "localhost",port=8000, debug=True)
    
    


