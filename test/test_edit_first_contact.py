from model.contact import Contact


def test_edit_fname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test", None, None))
    app.contact.edit_first_contact(Contact('Modified', None, None ))


def test_edit_lname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test", None, None))
    app.contact.edit_first_contact(Contact(None, None, 'Modified' ))
