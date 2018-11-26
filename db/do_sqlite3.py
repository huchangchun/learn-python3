#coding:utf-8
import os
import sqlite3
from sqlalchemy import Column, String ,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    #表的名字
    __tablename__ = 'user'
    
    #表的结构
    id = Column(String(20),primary_key = True)
    name = Column(String(20))
    score = Column(Integer)



def createTable():
   
    if os.path.isfile(db_file):
        os.remove(db_file)
        
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()
 
    
def get_score_in(low,high):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        
    except Exception as e:
        raise e
    else:
        #cur.execute('select name from user where score between ? and ? order by score',(low,high))
        cur.execute('select name from user where score between {0} and {1} order by score'.format(low,high))
        values = cur.fetchall()
        values = list(map(lambda x:x[0],values))
        cur.close()
        print(values)
        return values
    finally:
        conn.close()

def add_user():

    engine = create_engine('sqlite:///{0}'.format(db_file))
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    new_user = User(id='A-004', name='Bob', score=91)
    session.add(new_user)
    session.commit()
    session.close()    
def query_user(username):
    engine = create_engine('sqlite:///{0}'.format(db_file))
    DBSession = sessionmaker(bind=engine)
    session = DBSession()    
    userobj = session.query(User).filter(User.id==username).one()
    print('type',type(userobj))
    print('name',userobj.name)   
    session.close()   
if __name__=='__main__':
    db_file = os.path.join(os.path.dirname(__file__),'test.db')
     
    createTable()
    assert get_score_in(80, 95) == ['Adam'] 
    assert get_score_in(60, 80) == ['Bart', 'Lisa'] 
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'] 
    add_user()
    assert get_score_in(60, 100) == ['Bart', 'Lisa','Bob', 'Adam'] 
    query_user("A-001")
 
 