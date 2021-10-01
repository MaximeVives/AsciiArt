import string


class AsciiArt:
    def __init__(self):
        self.l = int(input())
        self.h = int(input())
        self.t = input().lower()
        self.word_list = []
        self.letters = self.initialize_alphabet_ascii()
        self.adjust_unknow_char()

        self.result = ""
        self.print_ascii_letter()

    def print_ascii_letter(self):
        for lettre in self.t:
            if lettre == "?":
                ascii_letter_list = self.letters[26]
            else:
                ascii_letter_list = self.letters[string.ascii_lowercase.index(lettre.lower())]

            self.word_list.append(ascii_letter_list)

        for hot in range(self.h):
            for word in self.word_list:
                # print(word[hot], end="")
                self.result += word[hot]
            # print("")
            self.result += "\n"
        self.result = self.result.rstrip() + " "

    def initialize_alphabet_ascii(self):
        ltrs = [[] for _ in range(28)]
        for _ in range(self.h):
            row = input()
            initial = 0
            for letter_incr, k in enumerate(range(self.l, len(row) + self.l, self.l)):
                ltrs[letter_incr].append(row[initial:k])
                initial = k

        return ltrs

    def adjust_unknow_char(self):
        for ind, ltr in enumerate(self.t):
            if ltr not in string.ascii_lowercase:
                self.t = self.t.replace(ltr, "?")
