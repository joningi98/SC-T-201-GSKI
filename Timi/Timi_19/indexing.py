from sortedcontainers import SortedDict


class Contact:
    def __init__(self, name='', phone_number='', email=''):
        self.name = name
        self.phoneNumber = phone_number
        self.email = email

    def __str__(self):
        return 'Name: {}, Phone number: {}, Email: {}'.format(self.name, self.phoneNumber, self.email)


class ContactList:
    def __init__(self):
        self.contact_map = SortedDict()
        self.name_map = SortedDict()
        self.phone_map = SortedDict()
        self.email_map = SortedDict()
        self.size = 0
        self.counter = 1

    def add_contact(self, name='', phone_number='', email=''):
        self.contact_map[self.counter] = Contact(name, phone_number, email)
        self.name_map[name] = self.counter
        self.phone_map[phone_number] = self.counter
        self.email_map[email] = self.counter
        self.counter += 1
        self.size += 1

    def get_by_name(self, name):
        n_id = self.name_map[name]
        return self.contact_map[n_id]

    def get_by_phone(self, phone):
        p_id = self.phone_map[phone]
        return self.contact_map[p_id]

    def get_by_email(self, email):
        e_id = self.email_map[email]
        return self.contact_map[e_id]

    def get_by_id(self, c_id):
        return self.contact_map[c_id]

    def remove(self, c_id):
        contact = self.contact_map[c_id]
        del self.name_map[contact.name]
        del self.phone_map[contact.phone_number]
        del self.email_map[contact.email]
        del self.contact_map[c_id]
        self.size -= 1

    def get_contacts_ordered_by_name(self):
        name_list = self.name_map.irange('ga', 'hzzz')
        ordered_name_list = []
        for name in name_list:
            ordered_name_list.append(self.contact_map[self.name_map[name]])
        return ordered_name_list


contact_list = ContactList()
contact_list.add_contact("Hanna Hönnudóttir", "1234567", "hanna@hanna.is")
contact_list.add_contact("Jón Jónsson", "2345678", "jon@jon.is")
contact_list.add_contact("Anna Önnudóttir", "3456789", "anna@anna.is")
contact_list.add_contact("Guðmundur Guðmundsson", "4567890", "gummi@gummi.is")
contact_list.add_contact("Bryndís Bryndísardóttir", "0123456", "disa@disa.is")
some_contact_1 = contact_list.get_by_name("Anna Önnudóttir")
some_contact_2 = contact_list.get_by_phone("4567890")
some_contact_3 = contact_list.get_by_email("hanna@hanna.is")
ordered_contact_list = contact_list.get_contacts_ordered_by_name()
for contact in ordered_contact_list:
    print(contact.name)
