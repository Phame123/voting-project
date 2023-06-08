#!/usr/bin/env python3
from flask import Blueprint, session
app = Blueprint('Main', __name__)
management = session
from api.verification import *
from api.ballotpages import *
from api.summary import *
