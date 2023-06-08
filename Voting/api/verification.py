#!/usr/bin/env python3
from Models.Voted import Voted
from Models.voters import Voter
from Models.Presido import Predo

from flask import render_template, request, url_for, redirect
from api import app
from api import management
from Storage import storage

@app.route('/Voting', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("Home.html")
    else:
        #Check for verification
        index = request.form.get("index")
        password = request.form.get("password")
        verify = storage.verification(index, password)
        if verify == 1:
            return render_template("Home.html", alert=True, message="Please you have already Voted!")
        elif verify == 2:
            return render_template("Home.html", alert=True, message="Please only DRATSA student are eligible to Vote!, Check you index and try again")
        elif verify == 4:
            return render_template("Home.html", alert=True, message="Password not Correct")
        else:
            management["name"] = storage.get_voter(index).name
            management["index"] = index
            return redirect(url_for("Main.president"))






