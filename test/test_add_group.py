# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("test", "test", "test"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.session.logout()



