"""
Database conection and generic read & write functions
"""
import pymysql

server = {
    "host": "localhost",
    "user": "cfm",
    "passwd": "1T3r0Nrul3z*w-t-f",
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


def insert_into_table(table="", columns="", data=()):
    """
    Generic code for inserting data into a table.
    table: name of the table(s)
    columns: A string containing the columns separated by comma
    data: A tuple containing the data to be inserted corresponding to the
             columns in 'columns'
    """
    conn, cursor = connect()

    #Add correct number of '%s' for the VALUES function
    params = "%s"
    i = len(data) - 1
    while i > 0:
        params += ", %s"
        i -= 1
    print("params: {}".format(params))
    query = """
        INSERT INTO
        {}({})
        VALUES({});
    """.format(table, columns, params)
    print("query: {}".format(query))

    cursor.execute(query, data)
    conn.commit()
    conn.close()


def update_table(table="", set_string="", data=(), where_string =""):
    """
    Generic code for updateing a table.
    table: name of the table(s)
    set_string: A string containing the columns to be update_details
                e.g "name = %s, id = %s"
    data: A tuple containing the data
    where_string: A string containing the where constraint
                  e.g  "name = %s, id = %s"
    """

    conn, cursor = connect()
    query = """
        UPDATE {}
        SET {}
        WHERE {}
    """.format(table, set_string, where_string)

    cursor.execute(query, data)
    conn.commit()
    conn.close()



def fetch_from_table(
                    required_columns="*",
                    where_clause="%s",
                    params=(1, ),
                    table='programme',
                    order=""):
    """
    Fetch required data from any table in the the database
    required_columns: A string containing the columns required from the
                      query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters

    Output: A list of dictionaries if the query is successful otherwise it
            returns False
    """
    db, cursor = connect()
    query = """
    SELECT {}
    FROM {}
    WHERE {}
    {};
    """.format(required_columns, table, where_clause, order)

    print("params = ", params)
    print("query: {}".format(query))
    try:
        cursor.execute(query, params)
    except Exception as error:
        data = False   #signify error
        print(str(error)) #Send to uwsgi log
    else:
        data = cursor.fetchall()

    db.close
    return data
