# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact("Ivan", "Ivanovich", "Ivanov"))


def test_create_empty_contact(app):
    app.contact.create(Contact("", "", ""))
