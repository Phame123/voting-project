#!/usr/bin/env python3
from Models import Base
from sqlalchemy import Column, String


class VotedFin(Base):
    __tablename__ = 'votedFin'
    index = Column(String(255), nullable=False, primary_key=True)

    def __init__(self, index):
        self.index = index
