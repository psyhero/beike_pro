# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from sqlalchemy import Column,Integer,String,PickleType
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+pymysql://root:mm546896@localhost:3306/beike'
db = declarative_base()

class DBItem(db):
    __tablename__ = 'zufang'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(55))
    rent = Column(Integer)
    addr = Column(PickleType)
    info = Column(PickleType)
    remark = Column(PickleType)
    supplier = Column(String(10))


class BeikeItem(scrapy.Item):
    title = scrapy.Field()
    rent = scrapy.Field()
    addr = scrapy.Field()
    info = scrapy.Field()
    remark = scrapy.Field()
    supplier = scrapy.Field()
