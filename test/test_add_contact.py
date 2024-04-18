# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact("Ivan", "Ivanovich", "Ivanov"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact("", "", ""))
    app.logout()
