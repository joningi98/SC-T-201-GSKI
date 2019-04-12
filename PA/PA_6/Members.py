import os
from sortedcontainers import SortedDict
from PA.PA_6.Sports import Sport


class Member:
    def __init__(self, name, phone, email, year_of_birth):
        self.name = name
        self.phone = phone
        self.email = email
        self.year_of_birth = year_of_birth
        self.sports = []

    def __str__(self):
        return "\n------------\n" \
               "Name: {}\n" \
               "Phone number: {}\n" \
               "Email: {}\n" \
               "Year of birth: {}\n" \
               "Sports: {}".format(self.name, self.phone, self.email, self.year_of_birth, [str(x) for x in self.sports])


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Members:
    def __init__(self):
        self.contact_map = SortedDict()
        self.name_map = SortedDict()
        self.phone_map = SortedDict()
        self.email_map = SortedDict()
        self.year_of_birth_map = SortedDict()
        self.size = 0
        self.counter = 1

    def add_member(self, name='', phone_number='', email='', year_of_birth=''):
        self.contact_map[self.counter] = Member(name, phone_number, email, year_of_birth)
        self.name_map[name] = self.counter
        self.phone_map[phone_number] = self.counter
        self.email_map[email] = self.counter
        self.year_of_birth_map[year_of_birth] = self.counter
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

    def get_by_year(self, year):
        return self.contact_map[year]

    def remove(self, c_id):
        contact = self.contact_map[c_id]
        del self.name_map[contact.name]
        del self.phone_map[contact.phone_number]
        del self.email_map[contact.email]
        del self.contact_map[c_id]
        self.size -= 1

    def get_all_members(self):
        global name_list
        get_member_action = input("Sort by\n"
                                  "1. Name\n"
                                  "2. Age\n"
                                  "3. Sport\n")
        if get_member_action == "1":
            name_list = self.name_map.irange('ga', 'hzzz')
        if get_member_action == "2":
            name_list = self.year_of_birth_map.irange(1, 99999999)
        if get_member_action == "3":
            pass
            # TODO: Fix get members by sport
            # name_list = self.s.irange('ga', 'hzzz')
        ordered_name_list = []
        for name in name_list:
            ordered_name_list.append(self.contact_map[self.name_map[name]])
        return ordered_name_list

    def __str__(self):
        members = self.get_all_members()
        my_str = ""
        for member in members:
            my_str += member + "\n"
        return my_str


class Members_UI:
    def __init__(self):
        self.members = Members()

    def main_menu(self):
        os.system('cls')
        action = ""
        while action != "5":
            action = input("\n1. Register new member\n"
                           "2. Get information from a member\n"
                           "3. Get all members\n"
                           "4. Remove member\n"
                           "5. Go back\n")
            if action == "1":
                self.__add_member()
            if action == "2":
                self.__get_one_member()
            if action == "3":
                self.__get_all_members()
            if action == "4":
                self.__remove_member()

    def __add_member(self):
        print("\n--New Member--")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        year_of_birth = input("Year of birth: ")
        self.members.add_member(name, phone, email, year_of_birth)

    def __get_one_member(self):
        global selected_member
        get_member_action = input("Get member by\n"
                                  "1. Name\n"
                                  "2. Phone\n"
                                  "3. Email\n"
                                  "4. Year of birth\n")
        if get_member_action == "1":
            name = input("Enter name: ")
            selected_member = self.members.get_by_name(name)
        if get_member_action == "2":
            phone = input("Enter Phone number: ")
            selected_member = self.members.get_by_phone(phone)
        if get_member_action == "3":
            email = input("Enter email: ")
            selected_member = self.members.get_by_email(email)
        return selected_member

    def __get_all_members(self):
        print(self.members)

    def __remove_member(self):
        member_to_rm = self.__get_one_member()
        c_id = self.members.get_by_phone(member_to_rm.phone)
        self.members.remove(c_id)


Ui = Members_UI()

Ui.main_menu()
