from PA.PA_6.Members import Member


class Sport:
    def __init__(self, name):
        self.name = name
        self.members = {}
        self.counter = 0

    def add_member_to_sport(self, new_member):
        unique_id = self.counter

    def __str__(self):
        return self.name





def main_menu():
    member_actions = M
    action = ""
    while action != "q":
        print("\n"
              "        1.Sports\n\n"
              "        2.Members\n\n"
              "        Q to quit\n")
        action = input()
        if action == "1":
            pass
        if action == "2":
            pass
