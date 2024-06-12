import re
from random import randrange

from model.contact import Contact
from test.test_phones import merge_phones_like_on_homepage


def test_compare_to_info_on_homepage(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.first_name == contact_from_edit_page.first_name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1.strip(), contact.email2.strip(), contact.email3.strip()])))


def test_all_contacts_to_db(app, db):
    contacts_hp = app.contact.get_contacts_list()
    contacts_db = db.get_contacts_list()
    assert len(contacts_hp) == len(contacts_db)
    contacts_hp = sorted(contacts_hp, key=Contact.id_or_max)
    contacts_db = sorted(contacts_db, key=Contact.id_or_max)
    assert contacts_hp == contacts_db
    for i in range(len(contacts_db)):
        assert contacts_hp[i].first_name == contacts_db[i].first_name
        assert contacts_hp[i].last_name == contacts_db[i].last_name
        assert contacts_hp[i].address == contacts_db[i].address
        assert contacts_hp[i].all_phones_from_homepage == merge_phones_like_on_homepage(contacts_db[i])
        assert contacts_hp[i].all_emails_from_homepage == merge_emails_like_on_homepage(contacts_db[i])
