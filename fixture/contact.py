from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init user creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_info(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name('selected[]')[index].click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.contacts_cache = None

    def delete_contact_by_id(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.contacts_cache = None

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_info(contact)
        # update info
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def edit_contact_by_id(self, contact_id, new):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(contact_id)
        self.fill_contact_info(new)
        # update info
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact edition
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact edition
        wd.find_element_by_css_selector("a[href='edit.php?id={}']".format(index)).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home page").click()

    def fill_contact_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name('entry'):
                cells = element.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                contact_id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contacts_cache.append(Contact(first_name=first_name, last_name=last_name,
                                                   contact_id=contact_id, address=address,
                                                   all_emails_from_homepage=all_emails,
                                                   all_phones_from_homepage=all_phones))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name,
                       contact_id=contact_id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone,
                       address=address, email1=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)


