#!/user/bin/env python3
"""Creates President database"""
from Models import Base
from sqlalchemy import Column, String, Integer, Float


class Org_sec(Base):
    __tablename__ = 'Organizing_secretary'
    name = Column(String(255), nullable=False)
    id = Column(Integer, autoincrement=True, primary_key=True)
    number_of_votes = Column(Integer)
    pic_name = Column(String(255), nullable=False)
    percentage = Column(Float, default=0)
    position = Column(Integer)

    def __init__(self, *args, **kwargs):
        for key,value in kwargs.items():
            self.__setattr__(key, value)