#!/usr/bin/env python3
from Models.voters import Voter
from Models.Officers import Officer
from Storage import storage

list_te = storage.get_candidates(Voter)
with open("user_data.txt", 'w') as file:
    file.write(f'{"Name":<35}{"Index":<20}{"Password":<15}{"Phone":<15}\n')
    for voter in list_te:
        file.write(f'{voter.name:<35}{voter.index:<20}{voter.password:<10}{voter.phone:<10}\n')
