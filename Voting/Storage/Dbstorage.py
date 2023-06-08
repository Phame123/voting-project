#!/usr/bin/env python
"""
Connecting to the  Alchemy
"""

from Models import Base
from Models.Presido import Predo
from Models.voters import Voter
from Models.Voted import Voted
from Models.Wcom import Wcom
from Models.General_secretary import Gen_sec
from Models.Financial_secretary import Fin_sec
from Models.Organizing_secretary import Org_sec
from Models.Public_realtions_oficer import PRO
from Models.VotedPresident import VotedPres
from Models.VotedPro import VotedPro
from Models.VotedWcom import VotedWcom
from Models.VotedGensec import VotedGen
from Models.VotedFinSec import VotedFin
from Models.VotedGensec import VotedGen
from Models.VotedOrgSec import VotedOrg
from Models.Officers import Officer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Storage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://root:root@localhost/test')
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def add(self, candidate):
        self.__session.add(candidate)
        self.__session.commit()


    def Check_voter_index(self, index):
        result = self.__session.query(Voter).\
            filter(Voter.index == index).first()
        return True if result else False

    def already_voted(self, index):
        result = self.__session.query(Voted).\
            filter(Voted.index == index).first()
        return True if result else False

    def increase_vote(self, id, position):
        aspirant = self.__session.query(position).\
            filter(position.id == id).first()
        if aspirant.number_of_votes:
            aspirant.number_of_votes += 1
        else:
            aspirant.number_of_votes = 1
        self.__session.commit()

    def get_voter(self, index):
        """
        get_voter: Returns a student voter instance
        :param index: To fetch
        :return: Instance of a voter
        """
        return self.__session.query(Voter).filter(Voter.index == index).first()

    def get_voter_second(self, cls, index):
        """
        get_voter: Returns a student voter instance
        :param index: To fetch
        :return: Instance of a voter
        """
        val = self.__session.query(cls).filter(cls.index == index).first()
        return True if val else False

    def verification(self, index, password):
        voter = self.get_voter(index)
        if voter:
            if self.already_voted(voter.index):
                return 1  # if user has already voted
            elif voter.password != password:
                return 4  # check password
            else:
                return 3  # check

        else:
            return 2  # voter is not eligible to vote

    def get_candidates(self, category):
        return list(self.__session.query(category))

    def verify_officer(self, index, password):
        officer = self.__session.query(Officer).filter(Officer.index == index).first()
        if officer:
            if officer.password == password: # has correctly login
                return 1
            else:
                return 2  # password don't match
        else:
            return 3  # not an officer

    def get_password(self, index):
        voter = self.get_voter(index)
        if voter:
            return voter.password
        else:
            return None

    def get_category_order(self, cat, cls):
        t = {}
        total = self.get_total_votes(cls)
        cat = list(self.__session.query(cat).order_by(cat.number_of_votes.desc()))
        result = []
        if total != 0:
            pos = 1
            for asparant in cat:
                if not asparant.number_of_votes:
                    t['number_of_votes'] = 0
                else:
                    t['number_of_votes'] = asparant.number_of_votes
                t['percentage'] = str((t["number_of_votes"] / total) * 100)[0:5]
                t['position'] = pos
                t['name'] = asparant.name
                t["pic_name"] = asparant.pic_name
                result.append(t)
                t = {}
                pos += 1
        else:
            pos = 0
            for asparant in cat:
                t['number_of_votes'] = 0
                t["position"] = pos
                t["name"] = asparant.name
                t['pic_name'] = asparant.pic_name
                pos += 1
        return result

    def get_officer(self, index):
        return self.__session.query(Officer).filter(Officer.index == index).first()

    def get_total_votes(self, cls):
        return self.__session.query(cls).count()

    def truncate(self, cls):
        self.__session.query(cls).delete()
        self.__session.commit()

    def resetElection(self, cls):
        result = self.__session.query(cls)
        for value in result:
            value.number_of_votes = 0
        self.__session.commit()
