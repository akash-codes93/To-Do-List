from conf import DATABASES as db
import pymysql


user = db.get('default').get('USER')
password = db.get('default').get('PASSWORD')
host = db.get('default').get('HOST')
database = db.get('default').get('NAME')



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def insert_query(query):

    status = None
    cnx = None

    try:
        cnx = pymysql.connect(user=user, password=password, host=host, database=database)
        cur = cnx.cursor()
        try:
            status = cur.execute(query)
            cnx.commit()

        except Exception as e:
            status = str(e)

        finally:
            cur.close()

    except Exception as e:

        status = str(e)

    finally:
        if cnx is not None:
            cnx.close()

    return status


def list_query(query):
    status = None
    cnx = None

    try:
        cnx = pymysql.connect(user=user, password=password, host=host, database=database)
        cur = cnx.cursor()
        try:
            cur.execute(query)
            status = dictfetchall(cur)

            cnx.commit()

        except Exception as e:
            status = str(e)

        finally:
            cur.close()

    except Exception as e:

        status = str(e)

    finally:
        if cnx is not None:
            cnx.close()

    return status


def delete_query(query):
    status = None
    cnx = None

    try:
        cnx = pymysql.connect(user=user, password=password, host=host, database=database)
        cur = cnx.cursor()
        try:
            status = cur.execute(query)

            cnx.commit()

        except Exception as e:
            status = str(e)

        finally:
            cur.close()

    except Exception as e:

        status = str(e)

    finally:
        if cnx is not None:
            cnx.close()

    return status





