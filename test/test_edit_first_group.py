from random import randrange

from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test", None, None))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='new')
    group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test", None, None))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group_new_header = Group(header="new")
    group_new_header.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, group_new_header)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index].header = group_new_header.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)