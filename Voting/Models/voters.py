#!/usr/bin/env python3
from Models import Base
from sqlalchemy import Column, String


class Voter(Base):
    __tablename__ = 'Voters'
    index = Column(String(255), nullable=False, primary_key=True)
    password = Column(String(255))
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
