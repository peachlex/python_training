from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test", None, None))
    app.group.edit_first_group(Group('new', None, None))


def test_edit_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test", None, None))
    app.group.edit_first_group(Group(None, "new", None))
