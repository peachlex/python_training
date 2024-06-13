from model.contact import Contact
from model.group import Group
import random

def test_remove_contact_from_group(app, db, orm, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create_contact(Contact(first_name="Test", last_name="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    contacts = orm.get_contacts_list()
    groups = orm.get_group_list()
    group = None
    for g in groups:
        if orm.get_contacts_in_group(g):
            group = g
            break

    if group is None:
        groups = db.get_group_list()
        app.contact.add_contact_in_group_by_id(groups[0])
        group = groups[0]

    old_list = len(orm.get_contacts_in_group(group))
    app.contact.delete_first_contact_from_group(some_group)
    count_contacts_after = len(orm.get_contacts_in_group(some_group))
    assert count_contacts_before - 1 == count_contacts_after
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)