# -*- coding: UTF-8 -*-
import json
import psycopg2
import uuid
connset="dbname='magnit3' user='python' host='localhost' password='python'"


def selectregion():
        try:
                conn = psycopg2.connect(connset)
        except:
                print "ne pashet"

        cur=conn.cursor()
        cur.execute("""SELECT regionid, regionname from region""")
        rows = cur.fetchall()
        js=json.dumps(rows)
        conn.close()
        return js                        
        

def selectcity(idregion):
        try:
                conn = psycopg2.connect(connset)
        except:
                print "ne pashet"
        
        cur=conn.cursor()
        cur.execute("""SELECT cityid, cityname from city WHERE regionid='"""+idregion+"'")
        rows = cur.fetchall()
        cities=json.dumps(rows)
        conn.close()
        return cities
        
def messtobase(messdict):
        try:
                conn = psycopg2.connect(connset)
        except:
                print "ne pashet"
        message=json.loads(messdict)        
        message['personid']=str(uuid.uuid4())
        
        cur=conn.cursor()
        cur.execute("""INSERT INTO persons(personid,lastname,firstname,fathername,cityid,phonenumber,mail,coment) VALUES (%(personid)s, %(lastname)s,%(firstname)s,%(fathername)s,%(cityid)s,%(phonenumber)s,%(mail)s,%(coment)s)""", message)
        conn.commit()
        conn.close()
    
def messread():
        try:
                conn = psycopg2.connect(connset)
        except:
                print "ne pashet"

        cur=conn.cursor()
        cur.execute("""SELECT personid, coment from persons""")
        rows = cur.fetchall()
        js=json.dumps(rows)
        conn.close()
        return js   

def messdelfrombase(personid):
        try:
                conn = psycopg2.connect(connset)
        except:
                print "ne pashet"
        cur=conn.cursor()
        persid=json.loads(personid)
        cur.execute("""DELETE from persons where personid='"""+persid+"'")
        conn.commit()
        conn.close()
          
