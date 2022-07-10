from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import Router, CPUUsage, engine

Session = sessionmaker(bind=engine)
session = Session()

session.query(CPUUsage).delete()
session.query(Router).delete()

session.commit()
