from random import randrange

from model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test", None))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact('Modified', 'Modified')
    contact.contact_id = old_contacts[index].contact_id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



