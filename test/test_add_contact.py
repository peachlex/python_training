# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Ivan", "Ivanovich", "Ivanov"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("", "", ""))
    app.session.logout()
