import getopt
import os.path
import sys
from model.contact import Contact
from generator.group import random_string
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Contact("", "")]+[
    Contact(first_name=random_string("fname", 6), last_name=random_string("lname", 8),
            homephone=random_string("home", 10), mobilephone=random_string("mobile", 10),
            workphone=random_string("work", 10), address=random_string("address", 10),
            email1=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(3)
    # Contact(first_name=fname, last_name=lname, homephone=hphone,
    #         mobilephone=mphone, workphone=wphone, address=address,
    #         email1=email, email2=email2, email3=email3
    #         )
    # for fname in ["", random_string("fname", 6)]
    # for lname in ["", random_string("lname", 8)]
    # for hphone in ["", random_string("home", 10)]
    # for mphone in ["", random_string("mobile", 10)]
    # for wphone in ["", random_string("work", 10)]
    # for address in ["", random_string("address", 10)]
    # for email in ["", random_string("email", 10)]
    # for email2 in ["", random_string("email2", 10)]
    # for email3 in ["", random_string("email3", 10)]

]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))