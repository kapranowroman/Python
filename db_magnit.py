# -*- coding: utf-8 -*-
import json
import psycopg2
import uuid
connset="dbname='magnit' user='python' host='localhost' password='python'"

def selectregion():
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        cur.execute("""SELECT regionid, regionname from region""")
        rows = cur.fetchall()
        js = json.dumps(rows)
        conn.close()
        return js
    except:
        print "not work"

def selectcity(idregion):
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        cur.execute("""SELECT cityid, cityname from city WHERE regionid=%s""", [idregion])
        rows = cur.fetchall()
        cities = json.dumps(rows)
        conn.close()
        return cities
    except:
        print "not work"

def messtobase(messdict):
    try:
        conn = psycopg2.connect(connset)
        message = json.loads(messdict)
        message['personid'] = str(uuid.uuid4())
        if message['cityid'] == '':
            message['cityid'] = '750edd5d-cfa0-47c6-aef0-78d67d0b20a5'
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO persons(personid,lastname,firstname,fathername,cityid,phonenumber,mail,coment)
            VALUES (%(personid)s, %(lastname)s,%(firstname)s,%(fathername)s,%(cityid)s,%(phonenumber)s,
            %(mail)s,%(coment)s)""", message)
        conn.commit()
        conn.close()
    except:
        print "not work"

def messread():
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        cur.execute("""SELECT personid, coment from persons""")
        rows = cur.fetchall()
        js = json.dumps(rows)
        conn.close()
        return js
    except:
        print "not work"

def messdelfrombase(personid):
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        persid = json.loads(personid)
        cur.execute("""DELETE from persons where personid=%s""", [persid])
        conn.commit()
        conn.close()
    except:
        print "not work"

def regstat():
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        cur.execute("""SELECT r.regionid , r.regionname, count(p.personid)
                    from persons p, city c, region r
                    where r.regionid = c.regionid
                    and c.cityid = p.cityid
                    group by r.regionid , r.regionname
                    having count(p.personid)>5""")
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        print "not work"

def citystat(regid):
    try:
        conn = psycopg2.connect(connset)
        cur = conn.cursor()
        cur.execute("""SELECT c.cityid , c.cityname, count(c.cityid)
                       from persons p, city c
                       where c.regionid = %s
                       and c.cityid = p.cityid
                       group by c.cityid , c.cityname""", [regid])
        rows = cur.fetchall()

        conn.close()
        return rows
    except:
        print "not work"
