import pymysql

server = {
    "host": "localhost",
    "user": "cfm",
    "passwd": "1T3r0Nrul3z*",
    "database": "programme_db"
}

def connect():
    """
    Connect to the mysql database.
    Returns a database connection and a cursor.
    """
    try:
        db = pymysql.connect(
            host = server["host"],
            user = server["user"],
            passwd = server["passwd"],
            db = server["database"]
        )
    except (ConnectionRefusedError) as cre:
        print("Error!: {} ".format(cre))
        exit()
    except (pymysql.err.OperationalError) as peoe:
        print("Error!: {}".format(peoe))
        exit()
    else:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

class User():
    """
    Class for handling users
    """

    def get_user_details(userid=None, username=None, firstname=None, lastname=None):
        """
        Get details about users from database;
        """
        params = 1
        if userid is not None:
            id_param = "id = '{}'".format(id)
            params = "{} and {}".format(params, id_param)
        if username is not None:
            un_param = "username = '{}'".format(username)
            params = "{} and {}".format(params, un_param)




        db, cursor = connect()
        query = """
        select *
        from user
        where {};
        """.format(params)
        print("query: {}".format(query))

        cursor.execute(query)
        user_details = cursor.fetchall()
        db.close
        return user_details
