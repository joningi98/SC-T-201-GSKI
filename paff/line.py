len_of_line = int(input())

my_list = []

for x in range(len_of_line):
    my_str = input()
    my_list.append(my_str)

new_list = []

for line in my_list:
    l_str = ""
    for ix, letter in enumerate(line):
        if ix == 0 and letter != ' ':
            new_letter = letter.upper()
            l_str += new_letter
        else:
            if letter == ' ':
                l_str += ' '
            elif letter != ' ':
                new_letter = letter.lower()
                l_str += new_letter
    print(l_str)
