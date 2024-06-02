# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact("Ivan", "Ivanovich", "Ivanov")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    print(new_contacts)
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print(old_contacts)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_empty_contact(app):
    app.contact.create(Contact("", "", ""))
