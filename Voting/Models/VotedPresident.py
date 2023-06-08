#!/usr/bin/env python3
from Models import Base
from sqlalchemy import Column, String


class VotedPres(Base):
    __tablename__ = 'votedPres'
    index = Column(String(255), nullable=False, primary_key=True)

    def __init__(self, index):
        self.index = index
