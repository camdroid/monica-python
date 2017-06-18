from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from config import db_host, db_pass

Base = declarative_base()

engine = create_engine("mysql+pymysql://cam:{}@{}/monica_py".format(db_pass, db_host),
                       connect_args= dict(host=db_host, port=3306), echo=True)

class Contact(Base):
    __tablename__ = 'contacts_1'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))


Base.metadata.create_all(engine)
 

