import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                list.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, lastname,address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(contact_id=str(id), first_name=firstname, last_name=lastname, address=address,
                                    homephone=home, mobilephone=mobile, workphone=work, email1=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()