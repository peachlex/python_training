from random import randrange

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
                            filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))
