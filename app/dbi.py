import pymysql
from bcrypt import gensalt, hashpw

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
    #print(server)
    try:
        db = pymysql.connect(
            host = server["host"],
            user = server["user"],
            passwd = server["passwd"],
            db = server["database"],
            autocommit=False
        )
    except (ConnectionRefusedError) as cre:
        print("Error!: {} ".format(cre))
        exit()
    except (pymysql.err.OperationalError) as peoe:
        print("Error!: {}".format(peoe))
        exit()
    except (pymysql.err.ProgrammingError) as pepe:
        print("Error!: {}".format(pepe))
        exit()
    else:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor


class User:
    """
    Class for handling users
    """
    def fetch_from_table(
                         required_columns="*",
                         where_clause="%s",
                         params=(1, ),
                         table='programme'):
        """
        Fetch required data from any table in the the database
        required_columns: A string containing the columns required from the
                          query or * for all
        where_clause: A string containg the statements after the where clause
        params: A tuple containing all the required parameters
        """

        db, cursor = connect()
        query = """
        select {}
        from {}
        where {};
        """.format(required_columns, table, where_clause)
        print("query: {}".format(query))

        cursor.execute(query, params)
        data = cursor.fetchall()
        db.close
        return data

    def get_user_details(required_columns="*", where_clause="%s", params=(1, )):
        """
        Get details about users from database
        required_columns: A string containing the columns required from the
                          query or * for all
        where_clause: A string containg the statements after the where clause
        params: A tuple containing all the required parameters
        """

        db, cursor = connect()
        query = """
        select {}
        from user
        where {};
        """.format(required_columns, where_clause)
        print("query: {}".format(query))

        cursor.execute(query, params)
        user_details = cursor.fetchall()
        db.close
        return user_details

    def add_department(name):
        """
        Add a department to the database.
        """
        conn, cursor = connect()

        query = """
            INSERT INTO
            department(name)
            VALUES(%s);
        """
        cursor.execute(query, (name, ))
        conn.commit()
        conn.close()

    def add_user(firstname, lastname, username, passwd, email, dept_id):
        """
        Save user details to database.
        """
        conn, cursor = connect()

        query = """
            INSERT INTO
            user(firstname, lastname, username, passwd, email, dept_id)
            VALUES(%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(
            query, (firstname, lastname, username, passwd, email, dept_id))
        conn.commit()
        conn.close()

    def add_topic(description):
        """
        Add a helpdesk topic to database.
        """
        conn, cursor = connect()

        query = """
            INSERT INTO
            topic(description)
            VALUES(%s);
        """
        cursor.execute(
            query, (description, ))
        conn.commit()
        conn.close()

    def check_pw(username, password):
        """
        Validate supplied usrname & password with the one in the database
        Output: True if successful
        """
        required_columns = "passwd"
        where_clause = "username = %s"
        params = [username]
        user_details = User.get_user_details(
            required_columns=required_columns,
            where_clause=where_clause,
            params=params)

        if user_details:
            valid_pw = bytes(user_details[0]["passwd"], 'utf8')
            return valid_pw == hashpw(password.encode("utf-8"), valid_pw)
        else:
            return False
