from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import json


Base = declarative_base()

class SignUp(Base):
    """Representation of class sign up"""
    __tablename__ = 'sign_up'

    id = Column(String(20), primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

    def __init__(self, id, name, password):
        """
        Constructor method that is called when a new instance of the SignUp class is created.
        It initializes the object with values for id, name, and password.

        """
        self.id = id
        self.name = name
        self.password = password

    def __repr__(self):
        """
        This function defines a string representation of the SignUp object.
        It returns a string containing the values of id, name, and password.
        """
        return "<SignUp(id='%s', name='%s', password='%s')>" % (self.id, self.name, self.password)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_list(self):
        return [self.id, self.name, self.password]

    def to_json_list(self):
        return json.dumps(self.to_list())

    def to_dict_list(self):
        return json.dumps(self.to_dict().values())

    def to_json_dict_list(self):
        return json.dumps(self.to_dict_list())
