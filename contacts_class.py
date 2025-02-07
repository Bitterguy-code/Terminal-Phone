# This will be used for the feature contacts code
# Create, update, delete, and read contacts

class Contacts:
    def __init__(self, contact_dict):
        self.contact_dict = {}

    # Create contact
    def create_contact(self):
        self.name = input("Enter the person's name: ")
        self.phone_num = input("Enter the phone number: ")
        self.contact_dict[self.name] = self.phone_num

    # Update contact
    def update_contact(self):
        look_up = input("Enter the person's name: ")

        # if in dict, update value
        if look_up in self.contact_dict.keys():
            new_num = input(f"We found {look_up}, enter the new number: ")
            self.contact_dict[look_up] = new_num

        #else, ask user if they want to create a contact
        else:
            print("Hmm we couldn't find that contact. Try creating a new contact instead.")
        
        
    # Delete contact
    def delete_contact(self):
        look_up = input("Enter the person's name: ")

        # if in dict, delete value
        if look_up in self.contact_dict.keys():
            self.contact_dict.pop(look_up)
            print("Contact deleted.")

        #else, ask user if they want to create a contact
        else:
            print("Hmm we couldn't find that contact. It may have already been deleted.")

    # Read Contacts
    def read_contacts(self):
        print("Here is your current contacts list: ")
        for person in self.contact_dict:
            print(f"Name: {person}, Number: {self.contact_dict[person]}")
        