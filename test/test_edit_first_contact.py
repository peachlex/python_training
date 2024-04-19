from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact('Modified', 'Modified', 'Modified' ))
    app.session.logout()