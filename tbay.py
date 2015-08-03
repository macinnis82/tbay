from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

class Item(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String)
  start_time = Column(DateTime, default=datetime.utcnow)
  
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  auction_item = relationship('Bid', backref='auction_item')
  
class User(Base):
  __tablename__= "users"

  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  
  #auction_item = relationship('Item', uselist=True, backref='user')
  bidder = relationship('Bid', backref='bidder')
  item = relationship('Item', backref='owner')
  
class Bid(Base):
  __tablename__ = "bids"
  
  id = Column(Integer, primary_key=True)
  price = Column(Float, nullable=False)
  
  bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
  
Base.metadata.create_all(engine)