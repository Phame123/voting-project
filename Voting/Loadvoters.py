#!/usr/bin/env python3
import os
from Models.voters import Voter
file_path = "voters"
from uuid import uuid4
from Storage import storage

with open(file_path, mode='r') as file:
    for line in file:
        if line != "\n":
            data = line.split(" ")
            number = 0
            if "/" in data[-1]:
                number = line[-1].split("/")[0]
            else:
                number = data[-1]
            number = number.replace("\n","")
            index = data[-2]
            name = str().join([name + " " for name in data[0:-2]])
            storage.add(Voter(**{"name": name,
                                 "phone": number,
                                 "password": str(uuid4())[0:4],
                                 "index": index}))

