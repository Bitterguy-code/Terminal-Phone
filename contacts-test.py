# test contacts class

from contacts_class import Contacts

# create an instance
new_contacts_list = Contacts({})

# test create fucntion
Contacts.create_contact(new_contacts_list)
Contacts.read_contacts(new_contacts_list)

# test update function
Contacts.update_contact(new_contacts_list)
Contacts.read_contacts(new_contacts_list)

# test delete function
Contacts.delete_contact(new_contacts_list)
Contacts.read_contacts(new_contacts_list)