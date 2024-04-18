

def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()