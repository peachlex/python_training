
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db, orm, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(first_name="Test", last_name="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        app.group.create_contact(Group(name="test"))
    contacts = orm.get_contacts_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    if len(orm.get_contacts_in_group(group)) > 0:
        app.contact.del_contact_from_group_by_id(contact.contact_id, group.group_id)
    app.contact.add_contact_in_group_by_id(contact.contact_id, group.group_id)
    new_contacts = orm.get_contacts_list()
    list_contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in list_contacts_in_group
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)