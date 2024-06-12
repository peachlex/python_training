import random
from random import randrange

from model.group import Group


def test_edit_name_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group("test", None, None))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name='new')
    new_group.group_id = group.group_id
    app.group.edit_group_by_id(group.group_id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(group_id=group.group_id, name=group.name.strip())
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



def test_edit_header_some_group(app):
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