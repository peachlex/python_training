import random
from random import randrange

from model.group import Group


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("test", "test", "test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(group_id=group.group_id, name=group.name.strip())
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
