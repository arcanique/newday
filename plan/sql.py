# coding=utf-8
import sqlite3 as sq

class sql:
    def __init__(self):
        self.conn = sq.connect("plan.db")
        self.memconn = sq.connect(":memory:")
        self.c = self.conn.cursor()

    def create_table(self,name):
        self.c.execute('''CREATE TABLE meta
                (ID INT PRIMARY KEY NOT NULL,
                NAME            TEXT NOT NULL,
                TYPE            TEXT NOT NULL,
                DEADLINE        INT  NOT NULL,
                INFO            TEXT);''')
        self.conn.commit()

    def insert(self):
        self.c.execute('''INSERT INTO meta (ID,NAME,TYPE,DEADLINE,INFO) VALUES (5, 'Pdasdasaul','x',3,'hahaasdh' )''')
        self.conn.commit()

    def update(self):
        self.c.execute(''' UPDATE meta SET TYPE = 'Texas' WHERE ID = 5;''')
        self.conn.commit()

    def query(self):
        return self.c.execute(''' SELECT * from meta WHERE type = 'new';''')
        #self.conn.commit()

    def delete(self):
        self.c.execute("DELETE from meta where ID=2;")
        self.conn.commit()


if __name__ == '__main__':
    a = sql()
   # a.create_table("1")
  #  a.adddata()
    a.update()
    a.delete()
    b = a.query()
    for a in b:
        print(a[0])
    print(b)