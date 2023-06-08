#!/usr/bin/evn python3
from Models.Officers import Officer
from uuid import uuid4
from Storage import storage

if __name__ == '__main__':
    Mustapha = Officer(**{"name":"Mustapha Gyarko Rafiatu", "index": "COH202018020", "password": str(uuid4())[0:4]})
    Ramon = Officer(**{"name":"Boafo Wiredu Raymon", "index": "COH202118024", "password": str(uuid4())[0:4]})
    storage.add(Mustapha)
    storage.add(Ramon)