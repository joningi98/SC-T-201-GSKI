class Sport:
    def __init__(self, name_of_sport):
        self.name_of_sport = name_of_sport
        self.members_in_sport = []

    def __str__(self):
        my_str = "---{}---".format(self.name_of_sport)
        for member in self.members_in_sport:
            my_str += str(member.name)
        return my_str



