# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Ivan", "Ivanovich", "Ivanov"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("", "", ""))
    app.session.logout()
