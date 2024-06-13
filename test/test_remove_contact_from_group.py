from model.contact import Contact
from model.group import Group
import random

def test_remove_contact_from_group(app, db, orm, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("test", "test", "test"))
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact("test", None, None))
    contacts = orm.get_contacts_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    target_group = random.choice(groups)
    if len(orm.get_contacts_in_group(target_group)) == 0:
        app.contact.add_contact_in_group_by_id(contact=contact, target_group=target_group)
    app.contact.remove_all_contacts_from_group(target_group)
    new_contacts = orm.get_contacts_list()
    contacts_in_group = orm.get_contacts_in_group(target_group)
    assert len(contacts_in_group) == 0
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)