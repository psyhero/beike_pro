# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .items import db,db_url,DBItem

class DBPipeline:
    def __init__(self) -> None:
        engine = create_engine(db_url)
        db.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def process_item(self, item, spider):
        db_item = DBItem(
            title = item['title'], 
            rent = item['rent'],
            addr = item['addr'],
            info = item['info'],
            remark = item['remark'],
            supplier = item['supplier'],
            )

        self.session.add(db_item)
        
        if len(self.session.new) >= 100 :
            self.session.commit()
            self.session.expunge_all()
       
        return item
    
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()


class BeikePipeline:
    def process_item(self, item, spider):
        return item
