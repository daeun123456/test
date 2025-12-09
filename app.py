import os
from flask import Flask, render_template,send_file, make_response,request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("./stealcompany.html")

@app.route("/freeboard")
def board_i():
    return send_file("stealcompany_board.html")

@app.route("/freeboard/<id>")
def board(id):
    id = int(id)
    if id == 0:
        return send_file("stealcompany_view.html")
    
    elif id == 1:
        return send_file("stealcompany_view_1.html")
    
    elif id == 2:
        return send_file("stealcompany_view_2.html")
    else:
        return make_response("Not Found", 404)
    
@app.route("/login", methods=["GET"])
def login():
    return send_file("stealcompany_login.html")

@app.route("/login_otp",methods=["GET"])
def login_otp():
    return send_file("stealcompany_login_otp.html")

@app.route("/login_otp", methods=["POST"])
def login_proc():
    otp_n = request.form.get("otp")
    if otp_n == "8":
        return redirect("/admin", 302)
    else:
        return make_response("Internal Error", 500)

@app.route("/admin")
def admin():
    return send_file("stealcompany_dashboard.html")


port = int(os.environ.get("PORT", 5555))

app.run(host="0.0.0.0", port=port)
