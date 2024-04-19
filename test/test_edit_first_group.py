from model.group import Group


def test_edit_first_group(app):
    app.session.login('admin', 'secret')
    app.group.edit_first_group(Group('modified', 'new header', 'new footer'))
    app.session.logout()