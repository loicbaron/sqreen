#!/usr/bin/env python3
import json
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, orm, types, UniqueConstraint

from project.config.database import Base, must_not_be_blank

class Obj(Base):
    """
    This class instantiates an Obj
    """
    __tablename__ = 'objects'
    id = Column(types.Integer, primary_key=True)
    attribute = Column(types.String(255))
    
    def __init__(self, **kwargs):
        super(Obj, self).__init__(**kwargs)

    def fromBlob(self, obj_dict):
        if "id" in obj_dict:
            self.id = obj_dict["id"]
        self.attribute = obj_dict["attribute"]
        return self

    def toJSON(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return "Object(attribute:{})".format(self.attribute)
    
    def __str__(self):
        return "attribute:{}".format(self.attribute)

