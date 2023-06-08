import json

from Models.Voted import Voted
from Models.voters import Voter
from Models.Presido import Predo
from Models.Wcom import Wcom
from Models.Public_realtions_oficer import PRO
from Models.Organizing_secretary import Org_sec
from Models.Financial_secretary import Fin_sec
from Models.General_secretary import Gen_sec
from Models.VotedPresident import VotedPres
from Models.VotedPro import VotedPro
from Models.VotedFinSec import VotedFin
from Models.VotedGensec import VotedGen
from Models.VotedWcom import VotedWcom
from Models.VotedOrgSec import VotedOrg



from flask import render_template, request, url_for, redirect
from api import app
from api import management
from Storage import storage

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # Check for verification
        index = request.form.get("index")
        password = request.form.get("password")
        verify = storage.verify_officer(index, password)
        if verify == 1:
            management["name"] = storage.get_officer(index).name
            management["index"] = index
            return redirect(url_for("Main.officerHome"))
        elif verify == 2:
            return render_template("login.html", alert=True, message="Password not Correct")
        else:
            return render_template("login.html", alert=True,
                                   message="Please you are not Officer, Check your index and try again")

@app.route("/officerhome")
def officerHome():
    if "name" in management:
        return render_template("officerHome.html")
    else:
        return redirect(url_for("Main.login"))

@app.route("/addstudent", methods=['GET', 'POST'])
def add_student():
    if "name" in management:
        if request.method == 'GET':
            return render_template('add.html')
        if request.method == "POST":
            name = request.form.get("name")
            index = request.form.get("index")

            password = request.form.get('password')
            cpassword = request.form.get('cpassword')
            if password != cpassword:
                return render_template("add.html", alert=True, message="Passwords dont match")
            elif storage.Check_voter_index(index):
                return render_template("add.html", alert=True, message="The student already exist")
            else:
                storage.add(Voter(**{"name": name, "password": password, "index": index, "phone": "xxxxxxx"}))
                return redirect(url_for("Main.officerHome"))
    else:
        return redirect(url_for('Main.login'))
@app.route('/showpassword', methods=['GET', 'POST'])
def show():
    if "name" in management:
        if request.method == "GET":
            return render_template('show.html')
        else:
            index = request.form.get('index')
            pwd = storage.get_password(index)
            if pwd:
                return render_template("show.html", password=pwd, index=index)
            else:
                return render_template("show.html", alert=True, message="Candidate not found")
    else:
        return redirect(url_for("Main.login"))


@app.route("/summary")
def summary():
    cat = storage.get_category_order(Predo, VotedPres)
    return render_template('statspage.html', title="PRESIDENTIAL SUMMARY", path="/static/images/presidents",total=storage.get_total_votes(VotedPres), category=cat)

@app.route("/finsec")
def finsec():
    cat = storage.get_category_order(Fin_sec, VotedFin)
    return render_template('statspage.html', title="FINANCIAL SECRETARY SUMMARY", path="/static/images/Fin_sec",total=storage.get_total_votes(VotedFin), category=cat)

@app.route("/gensec")
def gensec():
    cat = storage.get_category_order(Gen_sec, VotedGen)
    return render_template('statspage.html', title="GENERAL SECRETARY SUMMARY", path="/static/images/Gen_sec",total=storage.get_total_votes(VotedGen), category=cat)

@app.route("/orgsec")
def orgsec():
    cat = storage.get_category_order(Org_sec, VotedOrg)
    return render_template('statspage.html', title="ORGANIZING SECRETARY SUMMARY", path="/static/images/Org_sec", total=storage.get_total_votes(VotedOrg), category=cat)

@app.route("/prostat")
def prostat():
    cat = storage.get_category_order(PRO, VotedPro)
    return render_template('statspage.html', title="PRO SUMMARY", path="/static/images/Pro",total=storage.get_total_votes(VotedPro), category=cat)

@app.route("/wstat")
def wstat():
    cat = storage.get_category_order(Wcom, VotedWcom)
    return render_template('statspage.html', title="WCOM SUMMARY", path="/static/images/Wcom",total=storage.get_total_votes(VotedWcom), category=cat)
