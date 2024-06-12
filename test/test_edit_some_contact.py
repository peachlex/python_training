import random
from random import randrange

from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact("test", 'test'))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    new = Contact('Modified', 'Modified')
    new.contact_id = contact.contact_id
    # contact.contact_id = old_contacts[index].contact_id
    # app.contact.edit_contact_by_index(index, contact)
    index = old_contacts.index(contact)
    app.contact.edit_contact_by_id(contact.contact_id, new)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = new
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
