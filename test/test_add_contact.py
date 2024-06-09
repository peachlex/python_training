# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest

from test.test_add_group import random_string

testdata = [Contact("", "")]+[
    Contact(first_name=random_string("fname", 6), last_name=random_string("lname", 8),
            homephone=random_string("home", 10), mobilephone=random_string("mobile", 10),
            workphone=random_string("work", 10), address=random_string("address", 10),
            email1=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(3)
    # Contact(first_name=fname, last_name=lname, homephone=hphone,
    #         mobilephone=mphone, workphone=wphone, address=address,
    #         email1=email, email2=email2, email3=email3
    #         )
    # for fname in ["", random_string("fname", 6)]
    # for lname in ["", random_string("lname", 8)]
    # for hphone in ["", random_string("home", 10)]
    # for mphone in ["", random_string("mobile", 10)]
    # for wphone in ["", random_string("work", 10)]
    # for address in ["", random_string("address", 10)]
    # for email in ["", random_string("email", 10)]
    # for email2 in ["", random_string("email2", 10)]
    # for email3 in ["", random_string("email3", 10)]

]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

