#!/usr/bin/python3
"""The posts model for AfriDrop"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey


class Posts(BaseModel, Base):
    """Definition of Posts for products/services"""
    __tablename__ = 'posts'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=False)
    image = Column(String(255), nullable=True)
    price = Column(Integer, nullable=True)

    def __init__(self, user_id, title, description, image=None, price=None, *args, **kwargs):
        """Initializes Post"""
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.title = title
        self.description = description
        self.image = image
        self.price = price
