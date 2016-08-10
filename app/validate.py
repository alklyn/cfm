"""
A collection of procedures for validating user input.
"""
from flask import request
from werkzeug.exceptions import HTTPException
from app.dbi_read import prep_select
from app.forms import TicketForm


def update_selectors():
    """
    Update create_ticket form to display the location selector that is
    dependent on the one just selected.
    For example the selector for district will not be shown until the selector
    for province has been set
    """
    form = TicketForm()
    province_set = False
    district_set = False
    ward_set = False

    try:  #Check if the province is selected
        if request.form["province"] != "0":
            province_set = True
            province_id = int(request.form["province"])
            #list of id, district tuples
            districts = prep_select(table="district",
                                    constraint=province_id)
            form.district.choices = districts
    except (AttributeError, NameError, HTTPException) as error:
        message = str(error)

    try:  #Check if the district is selected
        if request.form["district"] != "0":
            district_set = True
            district_id = int(request.form["district"])
            #list of id, ward tuples
            wards = prep_select(table="ward", constraint=district_id)
            form.ward.choices = wards
    except (AttributeError, NameError, HTTPException) as error:
        message = str(error)

    try:  #Check if the ward is selected
        if request.form["ward"] != "0":
            ward_set = True
    except (AttributeError, NameError, HTTPException) as error:
        message = str(error)

    return form, province_set, district_set, ward_set
