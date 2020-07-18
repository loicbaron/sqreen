#!/usr/bin/env python3
import json
from dataclasses import dataclass
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, orm, types, UniqueConstraint
from uuid import uuid4

from project.config.database import Base, must_not_be_blank

@dataclass
class Event(Base):
    """
    This class instantiates an Event
    """
    __tablename__ = 'events'
    message_id: str = Column(types.String(255), primary_key=True)
    api_version: str = Column(types.Integer)
    date_created: str = Column(types.String(255))
    message_type: str = Column(types.String(255))
    retry_count: int = Column(types.Integer)
    message: str = Column(types.JSON)
    
    def __init__(self, message_id, api_version, date_created, message_type, retry_count, message):
        if message_id is None:
            message_id = str(uuid4())
        self.message_id = message_id
        self.api_version = api_version
        self.date_created = date_created
        self.message_type = message_type
        self.retry_count = retry_count
        self.message = message

    @classmethod
    def fromBlob(cls, event_dict):
        message_id = event_dict['message_id']
        api_version = event_dict['api_version']
        date_created = event_dict['date_created']
        message_type = event_dict['message_type']
        retry_count = event_dict['retry_count']
        message = event_dict['message']
        if isinstance(message, dict):
            message = json.JSONEncoder().encode(message)
        return cls(message_id, api_version, date_created, message_type, retry_count, message)

    def toJSON(self):
        return json.dumps({
            'message_id' : self.message_id,
            'api_version' : self.api_version,
            'date_created' : self.date_created,
            'message_type' : self.message_type,
            'retry_count' : self.retry_count,
            'message' : self.message
        })

    def __repr__(self):
        return "Event(message_id: {}, api_version: {}, date_created: {}, message_type: {}, retry_count: {}, message: {})"\
            .format(self.message_id, self.api_version, self.date_created, self.message_type, self.retry_count, self.message)
    
    def __str__(self):
        return "message_id: {}, api_version: {}, date_created: {}, message_type: {}, retry_count: {}, message: {}"\
            .format(self.message_id, self.api_version, self.date_created, self.message_type, self.retry_count, self.message)

