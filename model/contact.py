from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None,
                 contact_id=None, homephone=None, mobilephone=None,
                 workphone=None, all_phones_from_homepage=None,
                 address=None, email1=None, email2=None, email3=None,
                 all_emails_from_homepage=None):
        self.first_name = first_name
        self.last_name = last_name
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.contact_id = contact_id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.address = address
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s %s" % (self.contact_id, self.first_name, self.last_name)

    def __eq__(self, other):
        return ((self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)
                and self.last_name == other.last_name and self.first_name == other.first_name)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
