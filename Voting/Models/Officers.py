#!/user/bin/env python3
"""Creates President database"""
from Models import Base
from sqlalchemy import Column, String, Integer


class Officer(Base):
    __tablename__ = 'officers'
    name = Column(String(255), nullable=False)
    id = Column(Integer, autoincrement=True, primary_key=True)
    index = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    percentage = 0


    def __init__(self, *args, **kwargs):
        for key,value in kwargs.items():
            self.__setattr__(key, value)