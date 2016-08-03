import pymysql
from bcrypt import gensalt, hashpw

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
    user_details = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="user")
    return user_details


def get_gender(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about gender from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    genders = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="gender")
    return genders


def get_provinces(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about provinces from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    provinces = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="province")
    return provinces


def get_districts(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about districts from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    districts = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="district")
    return districts


def get_wards(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about wards from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    wards = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="ward")
    return wards


def get_villages(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about villages from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    villages = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="village")
    return villages


def get_partners(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about partners from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    partners = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="partner")
    return partners


def get_programmes(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about programmes from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    programmes = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="programme")
    return programmes


def get_topics(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about topics from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    topics = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="topic")
    return topics


def get_prioritys(required_columns="*", where_clause="%s", params=(1, )):
    """
    Get details about prioritys from database
    required_columns: A string containing the columns required from the
    query or * for all
    where_clause: A string containg the statements after the where clause
    params: A tuple containing all the required parameters
    """
    prioritys = fetch_from_table(required_columns=required_columns,
                                    where_clause=where_clause,
                                    params=params,
                                    table="priority")
    return prioritys


def prep_select(table="", constraint=""):
    """Prepare a list of id, user tuples for use in creating selectfields
    in forms.
    output: a list of tuples in as below:
    (id, "firstname lastname") for the user table.
    """
    if table == "user":
        required_columns = "id, firstname, lastname"
        user_details = get_user_details(required_columns=required_columns)
        data = [(0, "---Please Select Agent---")]
        for user in user_details:
            fullname = "{0} {1}".format(user["firstname"], user["lastname"])
            data.append((user["id"], fullname))

    elif table == "gender":
        required_columns = "id, description"
        genders = get_gender(required_columns=required_columns)
        data = [(0, "---Please Select Gender---")]
        for gender in genders:
            data.append((gender["id"], gender["description"]))

    elif table == "province":
        required_columns = "id, name"
        provinces = get_provinces(required_columns=required_columns)
        data = [(0, "---Please Select Province---")]
        for province in provinces:
            data.append((province["id"], province["name"]))

    elif table == "district":
        required_columns = "id, name"
        where_clause = "province_id = %s"
        params = (constraint,)
        districts = get_districts(required_columns=required_columns,
                                  where_clause=where_clause,
                                  params=params)
        data = [(0, "---Please Select District---")]
        for district in districts:
            data.append((district["id"], district["name"]))

    elif table == "ward":
        required_columns = "id, ward_number"
        where_clause = "district_id = %s"
        params = (constraint,)
        wards = get_wards(required_columns=required_columns,
                                  where_clause=where_clause,
                                  params=params)
        data = [(0, "---Please Select Ward---")]
        for ward in wards:
            data.append((ward["id"], ward["ward_number"]))

    elif table == "village":
        required_columns = "id, name"
        where_clause = "ward_id = %s"
        params = (constraint,)
        villages = get_villages(required_columns=required_columns,
                                  where_clause=where_clause,
                                  params=params)
        data = [(0, "---Please Select village---")]
        for village in villages:
            data.append((village["id"], village["name"]))

    elif table == "partner":
        required_columns = "id, name"
        partners = get_partners(required_columns=required_columns)
        data = [(0, "---Please Select Partner---")]
        for partner in partners:
            data.append((partner["id"], partner["name"]))


    elif table == "programme":
        required_columns = "id, name"
        programmes = get_programmes(required_columns=required_columns)
        data = [(0, "---Please Select Programme---")]
        for programme in programmes:
            data.append((programme["id"], programme["name"]))

    elif table == "topic":
        required_columns = "id, description"
        topics = get_topics(required_columns=required_columns)
        data = list()
        data = [(0, "---Please Select topic---")]
        for topic in topics:
            data.append((topic["id"], topic["description"]))

    elif table == "priority":
        required_columns = "id, description"
        prioritys = get_prioritys(required_columns=required_columns)
        data = [(0, "---Please Select Priority---")]
        for priority in prioritys:
            data.append((priority["id"], priority["description"]))

    return data


def insert_into_table(table="", columns="", data=()):
    """
    Generic database insertion code.
    table: name of the table
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


def add_department(name):
    """
    Add a department to the database.
    """
    table = "department"
    columns = "name"
    data = (name, )
    insert_into_table(table, columns, data)


def add_user(firstname, lastname, username, passwd, email, dept_id):
    """
    Save user details to database.
    """
    table = "user"
    columns = "firstname, lastname, username, passwd, email, dept_id"
    data = (firstname, lastname, username, passwd, email, dept_id)
    insert_into_table(table, columns, data)


def add_topic(description):
    """
    Add a helpdesk topic to database.
    """
    table = "topic"
    columns = "description"
    data = (description, )
    insert_into_table(table, columns, data)


def add_priority(description):
    """
    Add a ticket priority level to database.
    """
    table = "priority"
    columns = "description"
    data = (description, )
    insert_into_table(table, columns, data)


def add_ticket_status(description):
    """
    Add a ticket status level to database.
    """
    table = "ticket_status"
    columns = "description"
    data = (description, )
    insert_into_table(table, columns, data)


def add_ticket(
               firstname, lastname, phone_number, gender_id, ward_id, location,
               topic_id, priority_id, partner_id, programme_id, details,
               created_by, assigned_to):
    """
    Add a ticket  to database.
    """
    table = "ticket"
    columns = """
        firstname, lastname, phone_number, gender_id, ward_id, location,
        topic_id, priority_id, partner_id, programme_id, details, created_by,
        assigned_to
    """
    data = (
        firstname, lastname, phone_number, gender_id, ward_id, location,
        topic_id, priority_id, partner_id, programme_id, details, created_by,
        assigned_to)
    insert_into_table(table, columns, data)


def check_pw(username, password):
    """
    Validate supplied usrname & password with the one in the database
    Output: True if successful
    """
    required_columns = "passwd"
    where_clause = "username = %s"
    params = [username]
    user_details = get_user_details(
        required_columns=required_columns,
        where_clause=where_clause,
        params=params)

    if user_details:
        valid_pw = bytes(user_details[0]["passwd"], 'utf8')
        return valid_pw == hashpw(password.encode("utf-8"), valid_pw)
    else:
        return False


# def fetch_from_table(
#                     required_columns="*",
#                     where_clause="%s",
#                     params=(1, ),
#                     table='programme',
#                     select_stmt="select"):
def get_tickets(status_id=1):
    """
    Get ticket details from the db.
    Output:
        A list of dictionaries if any tickets are in the db.
        Each dictionary contains details of a particular ticket.
    """
    required_columns = """
    LPAD(a.id, 7, '0') as 'ticket_number',
    CONCAT(a.firstname, " ", a.lastname) as 'name',
    a.phone_number,
    b.`description` as 'gender',
    c.ward_number,
    a.location,
    d.description as 'topic',
    e.description as 'priority',
    f.name as 'partner',
    g.name as 'programme',
    a.details,
    CONCAT(h.firstname, " ", h.lastname) as 'rep',
    CONCAT(i.firstname, " ", i.lastname) as 'agent',
    j.description as 'status',
    a.dt_created
    """

    table = """
    ticket a
    INNER JOIN `gender` b ON b.id = a.gender_id
    INNER JOIN `ward` c ON c.id = a.ward_id
    INNER JOIN `topic` d ON d.id = a.topic_id
    INNER JOIN `priority` e ON e.id = a.priority_id
    INNER JOIN `partner` f ON f.id = a.partner_id
    INNER JOIN `programme` g ON g.id = a.programme_id
    INNER JOIN `user` h ON h.id = a.created_by
    INNER JOIN `user` i ON i.id = a.assigned_to
    INNER JOIN `ticket_status` j ON j.id = a.status_id
    """

    tickets = fetch_from_table(
        required_columns=required_columns,
        where_clause="status_id = %s",
        params=(status_id,),
        table=table)
    return tickets
