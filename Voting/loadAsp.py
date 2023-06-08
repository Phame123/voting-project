#!/usr/bin/python3
from Storage import storage
from Models.Presido import Predo
from Models.Wcom import Wcom
from Models.Public_realtions_oficer import PRO
from Models.Organizing_secretary import Org_sec
from Models.Financial_secretary import Fin_sec
from Models.General_secretary import Gen_sec

wcom = [ {"name": "Charlotte Osei", "pic_name": "osei.jpg"},
         {"name": "Lordina Mahama", "pic_name": "lordina.jpeg"},
         {"name": "Rebecca Akuffo Addo", "pic_name": "rebeca.jpeg"}]

org = [ {"name": "Kwasi Twum", "pic_name": "kwesi.jpeg"},
         {"name": "Kwaku Oteng", "pic_name": "kweku.jpeg"},
         {"name": "Kwame Despite", "pic_name": "kwame.jpeg"}]

pro = [ {"name": "Nana Aba Anamoah", "pic_name": "nana.jpeg"},
         {"name": "Bernard Avle", "pic_name": "benard.jpeg"},
         {"name": "Ameyaw Debrah", "pic_name": "ameyaw.jpeg"}]

fin = [ {"name": "Ken Ofori Atta", "pic_name": "ken.jpeg"},
         {"name": "Jean Mensah", "pic_name": "jean.jpeg"},
         {"name": "Seth Terkper", "pic_name": "seth.jpeg"} ]
pre = [ {"name": "John Dramani Mahama", "pic_name": "john.jpeg"},
         {"name": "Elsie Effah Kaufmann", "pic_name": "effa.jpeg"},
         {"name": "Bahomiah ", "pic_name": "baho.jpeg"} ]
gen = [ {"name": "Dr Kwabena Opoku-Adusei", "pic_name": "opoku.jpeg"},
         {"name": "Kofi Annan", "pic_name": "kofi.jpeg"},
         {"name": "Esiedu Nketia", "pic_name": "nketia.jpeg"} ]


def load():
    storage.truncate(Wcom)
    for cand in wcom:
        storage.add(Wcom(**cand))

    storage.truncate(Gen_sec)
    for cand in gen:
        storage.add(Gen_sec(**cand))

    storage.truncate(Org_sec)
    for cand in org:
        storage.add(Org_sec(**cand))

    storage.truncate(Fin_sec)
    for cand in fin:
        storage.add(Fin_sec(**cand))

    storage.truncate(PRO)
    for cand in pro:
        storage.add(PRO(**cand))

    storage.truncate(Predo)
    for cand in pre:
        storage.add(Predo(**cand))
