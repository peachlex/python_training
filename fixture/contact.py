from model.contact import Contact


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
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.contacts_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact edition
        wd.find_element_by_xpath('//img[@title="Edit"]').click()
        self.fill_contact_info(contact)
        # update info
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home page").click()

    def fill_contact_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)

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
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                contact_id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contacts_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id))
        return list(self.contacts_cache)
