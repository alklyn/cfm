"""
Various functions for reading from the database.
"""
from bcrypt import gensalt, hashpw
from app.dbi import fetch_from_table

server = {
    "host": "localhost",
    "user": "cfm",
    "passwd": "1T3r0Nrul3z*w-t-f",
    "database": "programme_db"
}


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

    elif table == "update_type":
        update_types = fetch_from_table(required_columns="id, description",
                                        table=table,
                                        order="order by id")
        data = [(0, "---Please Select Option---")]
        for update_type in update_types:
            data.append((update_type["id"], update_type["description"]))

    return data


def check_pw(username, password):
    """
    Validate supplied username & password with the one in the database
    Output: True if successful
    """
    required_columns = "passwd"
    where_clause = "username = %s"
    params = (username, )
    user_details = fetch_from_table(
        required_columns=required_columns,
        where_clause=where_clause,
        params=params,
        table="user")

    if user_details:
        valid_pw = bytes(user_details[0]["passwd"], 'utf8')
        return valid_pw == hashpw(password.encode("utf-8"), valid_pw)
    else:
        return False


def get_tickets(where_clause="status_id = %s", params=(1, )):
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
    a.dt_created,
    k.name as 'district',
    l.name as 'province',
    a.location
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
    INNER JOIN `district` k ON k.id = c.district_id
    INNER JOIN `province` l ON l.id = k.province_id
    """

    tickets = fetch_from_table(
        required_columns=required_columns,
        where_clause=where_clause,
        params=params,
        table=table)
    return tickets
