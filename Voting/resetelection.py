#!/usr/bin/python3
from Models.Wcom import Wcom
from Models.Presido import Predo
from Models.Financial_secretary import Fin_sec
from Models.General_secretary import Gen_sec
from Models.Public_realtions_oficer import PRO
from Models.Organizing_secretary import Org_sec
from Storage import storage
from Models.Voted import Voted
from Models.VotedPresident import VotedPres
from Models.VotedPro import VotedPro
from Models.VotedFinSec import VotedFin
from Models.VotedGensec import VotedGen
from Models.VotedWcom import VotedWcom
from Models.VotedOrgSec import VotedOrg
from loadAsp import load
if __name__ == '__main__':
    trunc = [Voted, VotedGen, VotedOrg, VotedPro, VotedPres, VotedFin, VotedWcom]
    load()
    for table in trunc:
        storage.truncate(table)
    print("Done")
