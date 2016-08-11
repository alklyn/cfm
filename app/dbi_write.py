from app.dbi import insert_into_table

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


def add_update(ticket_id, post, posted_by):
    """
    Insert a new update to a ticket into the database.
    """
    table = "ticket_update"
    columns = "ticket_id, post, posted_by"
    data = (ticket_id, post, posted_by)
    insert_into_table(table, columns, data)
