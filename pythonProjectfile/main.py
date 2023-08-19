from flask import Flask,render_template,request

from pymongo import MongoClient

client = MongoClient()
mydb = client.MEASI_STD_DB
mycol = mydb.std_details

webapp = Flask(__name__)
clg_py = "pullingo  technology"
@webapp.route("/")
def home():
    return render_template("home.html",clg_html = clg_py)

@webapp.route("/reg")
def reg():
    return render_template("reg.html")
@webapp.route("/booking" , methods = ["GET","POST"])
def booking():
    if request.method == "POST":
        un_login = request.form["username"]
        pd_login = request.form["password"]

        result = mycol.find_one({"$and": [{"uname": un_login}, {"pwd": pd_login}]},
                                {"_id": 0, "uname": 0, "pwd": 0})  # projection 1 = show, 0 = dont show
        if result == None:
            return "invalid user"
        else:
            return render_template("booking.html", result_html=result)  # jinja templating

        return render_template("booking.html")

@webapp.route("/get_ticket" , methods = ["GET","POST"])
def get_ticket():

    return render_template("get_ticket.html")

@webapp.route("/ack", methods = ["GET","POST"])
def ack():
    data = {}
    if request.method == "POST":

        data["name"] = request.form["name"]
        data["phone_number"] = request.form["phone_number"]
        data["email"] = request.form["email"]
        data["uname"] = request.form["username"]
        data["pwd"] = request.form["password"]

        # insert the collected data from students through register webpage
        mycol.insert_one(data)
        return render_template("ack.html")

@webapp.route("/login")
def login():

    return render_template("login.html")




@webapp.route("/dashboard",methods = ["GET","POST"])
def dash():
    if request.method == "POST":
       a= request.form["name"]
       b= request.form["email"]
       c = request.form["people"]
       d= request.form["time"]
       e= request.form["date"]
       f= request.form["number"]

       return render_template('dashboard.html',name=a,email=b,people=c,time=d,date=e,number=f)


if __name__=="__main__":
  webapp.run(debug=True)




# Initializing list
