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
    
    def __init__(self, id = None, attribute = ""):
        self.id = id
        self.attribute = attribute

    @classmethod
    def fromBlob(cls, obj_dict):
        if "id" in obj_dict:
            id = obj_dict["id"]
        else:
            id = None
        attribute = obj_dict["attribute"]
        return cls(id, attribute)

    def toJSON(self):
        return json.dumps({'id': self.id, 'attribute': self.attribute})

    def __repr__(self):
        return "Object(id: {}, attribute:{})".format(self.id, self.attribute)
    
    def __str__(self):
        return "id:{}, attribute:{}".format(self.id, self.attribute)

