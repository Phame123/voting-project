#!/usr/bin/env python3
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

@app.route("/predo", methods = ['GET', 'POST'])
def president():
    if 'name' in management:
        if not storage.get_voter_second(VotedPres, management.get("index")):
            if request.method == 'GET':
                presidents = storage.get_candidates(Predo)
                return render_template('Asparrant.html', count='1', pic_path="/static/images/presidents", cat="Presidential", category=presidents, name=management.get("name"), path=url_for('Main.president'))
            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, Predo)
                storage.add(VotedPres(management['index']))
                return redirect(url_for("Main.gen_sec"))
        else:
            return redirect(url_for("Main.gen_sec"))
    else:
        return redirect(url_for("Main.home"))

@app.route("/GenSec", methods=['GET', 'POST'])
def gen_sec():
    """
    Gen_sec : The General_sectary Page
    :return:
    """
    if "name" in management:
        if not storage.get_voter_second(VotedGen, management.get("index")):
            if request.method == 'GET':
                gen_secs = storage.get_candidates(Gen_sec)
                return render_template('Asparrant.html', count='2', pic_path="/static/images/Gen_sec",
                                       cat="General Secretory",
                                       category=gen_secs, name=management.get("name"),
                                       path=url_for('Main.gen_sec'))

            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, Gen_sec)
                storage.add(VotedGen(management["index"]))
                return redirect(url_for("Main.fin_sec"))
        else:
            return redirect(url_for("Main.fin_sec"))
    else:
        return redirect(url_for('Main.home'))

@app.route("/FinSec", methods=['GET', 'POST'])
def fin_sec():
    """
    fin_sec: Path for Financial Secretary
    :return: A page for fin to vote
    """
    if "name" in management:
        if not storage.get_voter_second(VotedFin, management.get("index")):
            if request.method == 'GET':
                fin_secs = storage.get_candidates(Fin_sec)
                return render_template('Asparrant.html', count='3',
                                       pic_path="/static/images/Fin_sec", cat="Financial Secretary",
                                       category=fin_secs, name=management.get("name"),
                                       path=url_for('Main.fin_sec'))
            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, Fin_sec)
                storage.add(VotedFin(management['index']))
                return redirect(url_for("Main.org_sec"))
        else:
            return redirect(url_for("Main.org_sec"))
    else:
        redirect(url_for("Main.home"))


@app.route("/OrgSec", methods=['GET', 'POST'])
def org_sec():
    """
    org_sec: Path for Organizing Secretary page
    :return: A page for fin to vote
    """
    if "name" in management:
        if not storage.get_voter_second(VotedOrg, management.get("index")):
            if request.method == 'GET':
                org_secs = storage.get_candidates(Org_sec)
                return render_template('Asparrant.html', count='4',
                                       pic_path="/static/images/Org_sec", cat="Organizing Secretary",
                                       category=org_secs, name=management.get("name"),
                                       path=url_for('Main.org_sec'))
            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, Org_sec)
                storage.add(VotedOrg(management['index']))
                return redirect(url_for("Main.pro"))
        else:
            return redirect(url_for("Main.pro"))
    else:
        redirect(url_for("Main.home"))


@app.route("/PRO", methods=['GET','POST'])
def pro():
    if "name" in management:
        if not storage.get_voter_second(VotedPro, management.get("index")):
            if request.method == 'GET':
                pro_secs = storage.get_candidates(PRO)
                return render_template('Asparrant.html', count='5',
                                       pic_path="/static/images/Pro", cat="Public Relation Officer",
                                       category=pro_secs, name=management.get("name"),
                                       path=url_for('Main.pro'))
            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, PRO)
                storage.add(VotedPro(management['index']))
                return redirect(url_for("Main.wcom"))
        else:
            return redirect(url_for("Main.wcom"))
    else:
        redirect(url_for("Main.home"))

@app.route("/wcom", methods=['GET', 'POST'])
def wcom():
    if "name" in management:
        if not storage.get_voter_second(VotedWcom, management.get("index")):
            if request.method == 'GET':
                wcoms = storage.get_candidates(Wcom)
                return render_template('Asparrant.html', count='6',
                                       pic_path="/static/images/Wcom", cat="Women Commissioner",
                                       category=wcoms, name=management.get("name"),
                                       path=url_for('Main.wcom'))
            else:
                candidate_id = request.form.get("candidate")
                storage.increase_vote(candidate_id, Wcom)
                storage.add(VotedWcom(management['index']))
                return redirect(url_for("Main.thanks"))
        else:
            return redirect(url_for("Main.thanks"))
    else:
        redirect(url_for("Main.home"))


@app.route("/thanks", methods=['GET', 'POST'])
def thanks():
    if "name" in management:
        if request.method == 'GET':
            return render_template('thanks.html', name=management['name'])
        else:
            management.pop("name")
            storage.add(Voted(management['index']))
            return redirect(url_for('Main.home'))
    else:
        redirect(url_for('Main.home'))
