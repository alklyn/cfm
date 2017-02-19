-- Staffmember's department
CREATE TABLE  department (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE gender (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE priority (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE programme (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE province (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE district (
    id SERIAL PRIMARY KEY,
    province_id INTEGER REFERENCES province(id) ON DELETE CASCADE,
    name TEXT NOT NULL
);

CREATE TABLE ward (
    id SERIAL PRIMARY KEY,
    district_id INTEGER REFERENCES district(id) ON DELETE CASCADE,
    ward_number INTEGER NOT NULL
);

CREATE TABLE fdp (
    id SERIAL PRIMARY KEY,
    district_id INTEGER REFERENCES district(id) ON DELETE CASCADE,
    name TEXT NOT NULL
);

CREATE TABLE agent (
    id SERIAL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    username TEXT NOT NULL,
    passwd TEXT NOT NULL,
    email TEXT NOT NULL,
    dept_id INTEGER REFERENCES department(id) ON DELETE CASCADE,
    dt_added TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE village (
    id SERIAL PRIMARY KEY,
    ward_id INTEGER REFERENCES ward(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    village_head TEXT,
    representative TEXT
);

CREATE TABLE ticket_status (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE update_type (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE partner (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE ticket (
    id SERIAL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    gender_id INTEGER REFERENCES gender(id) ON DELETE CASCADE,
    ward_id INTEGER REFERENCES ward(id) ON DELETE CASCADE,
    location TEXT NOT NULL,
    topic_id INTEGER REFERENCES topic(id) ON DELETE CASCADE,
    priority_id INTEGER REFERENCES priority(id) ON DELETE CASCADE,
    partner_id INTEGER REFERENCES partner(id) ON DELETE CASCADE,
    programme_id INTEGER REFERENCES programme(id) ON DELETE CASCADE,
    details TEXT NOT NULL,
    created_by INTEGER REFERENCES agent(id) ON DELETE CASCADE,
    assigned_to INTEGER REFERENCES agent(id) ON DELETE CASCADE,
    status_id INTEGER NOT NULL DEFAULT 1 REFERENCES ticket_status(id) ON DELETE CASCADE,
    dt_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE cfm.ticket.firstname IS 'First name of caller.';
COMMENT ON TABLE cfm.ticket.lastname IS 'Last name of caller.';
COMMENT ON TABLE cfm.ticket.phone_number IS 'Phone number of caller.';
COMMENT ON TABLE cfm.ticket.phone_number IS 'Village or other location where the caller is reporting about.';

CREATE TABLE ticket_update (
    id SERIAL PRIMARY KEY,
    type_id INTEGER REFERENCES update_type(id) ON DELETE CASCADE,
    ticket_id INTEGER REFERENCES ticket(id) ON DELETE CASCADE,
    post TEXT NOT NULL,
    posted_by INTEGER REFERENCES agent(id) ON DELETE CASCADE,
    dt_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
