from flask import Flask, render_template, flash,redirect, url_for, request
from flask_mysqldb import MySQL
import sqlite3 as sql
import pymysql

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


@app.route("/wrong_password")
def wrong_password_email():
    return render_template('wrong_password_email.html')




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
        c.execute("insert into edu_signup_details values('{}','{}','{}')".format(Email, password,user_name))
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
        c.execute("insert into children_details(NGO_Name, Email, Phone, City, NGO_registration_ID,Amount) values('{}','{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,NGO_registration_ID,Amount))
        conn.commit()
        conn.close()
        c.close()
    return render_template("children_request.html")

@app.route("/education_request_sent")
def education_request_sent():
    return render_template("education_request_sent.html")



    


# @app.route("/children_login", methods=["GET", "POST"])
# def children_login():
#     global children_email

#     if request.method == "POST":
        
#         children_email = request.form.get("email")
#         password = request.form.get("password")

        
#         if children_check_user(children_email, password):
#             return render_template('children_welcome.html')
#         else:
          
#             return render_template("children_wrong_password_email.html")
#     else:
#         # return render_template('children_login.html')
#         return children_email
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
    cur.execute("SELECT NGO_Name,email,status FROM children_details  where email=%s", (children_email,))
    
    rows = cur.fetchall()
    cur.close()
    return render_template('children_pending_request.html',rows=rows)
    # return children_email



def children_check_user(email, password):
    conn, c = sql_connector()
    
    c.execute("SELECT * FROM edu_signup_details WHERE Username=%s AND password=%s", (email, password))
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
        conn, c = sql_connector()
        c.execute("insert into farmer_details (Name,Email,Phone,Address,Farmer_ID) values('{}','{}','{}','{}','{}')".format(Name, Email,Phone,Address,Farmer_ID))
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
    cur.execute("SELECT count(*) FROM edu_details ")
    e_details = cur.fetchone()
    cur.execute("SELECT count(*) FROM edu_signup_details ")
    e_signup_details = cur.fetchone()
    cur.execute("SELECT count(*) FROM farmer_signup_details ")
    f_signup_details = cur.fetchone()

    cur.close()
    
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
   
    return render_template("admin.html",data=f_details,data2 = e_details,data3 = e_signup_details,data4 = f_signup_details,total = total_users)
    
    # return f_details

@app.route('/admin_users')
def admin_users():
    return render_template("admin_users.html")


@app.route('/admin_users/farmers')
def admin_user_farmer():
    
    cur = mysql.connection.cursor()
   
    
    cur.execute("SELECT Name, Email, Phone, Address, Farmer_ID, Status FROM farmer_details ")
    details = cur.fetchall()
  
    return render_template("admin_farmer_option.html",details=details)

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
   
    
    cur.execute("SELECT ID, NGO_NAME, Email, Phone, City, NGO_REGISTRATION_ID,AMOUNT,status FROM children_details ")
    details = cur.fetchall()
  
    return render_template("admin_NGO_option.html",details=details)
    # return details
    # return render_template("admin_NGO_option.html")


@app.route('/admin_users/NGO/update/<string:SL_No>', methods=['POST'])
def update_NGO_status(SL_No):
    sno = SL_No
    status = request.form['status']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE children_details SET Status = %s WHERE id = %s", (status, sno))
    mysql.connection.commit()
    cur.close()
    
    flash('Status updated successfully!', 'success')
    # return sno
    
    return redirect(url_for('admin_user_NGO'))


@app.route('/admin_users/donors')
def admin_user_donors():
    return render_template("admin_donors_option.html")


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