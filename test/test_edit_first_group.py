from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group('new', None, None))