import csv
import os

"""Style"""
R = '\x1b[31m'
G = '\x1b[32m'
B = '\x1b[34m'
W = '\x1b[37m'
Y = '\x1b[33m'
M = '\x1b[35m'
C = '\x1b[36m'
Bl = '\x1b[39m'

S_b = '\x1b[1m'
S_n = '\x1b[22m'


class Dictionary:
    """Name your datas file, default=data"""

    def __init__(self, name_file: str = "data"):

        self.name_file = f'{name_file}.csv'

        # file check
        try:
            os.stat(self.name_file).st_size == 0
        except FileNotFoundError:
            with open(self.name_file, "w", newline="", encoding="utf8"):
                pass

        self.header = ["English", "Transcript", "Translation"]

        if os.stat(self.name_file).st_size == 0:
            with open(self.name_file, "w", newline="", encoding="utf8") as f:
                writer = csv.DictWriter(f, fieldnames=self.header)
                writer.writeheader()

    def set_word(self, word_on_eng: str, transcript: str, translation: str):
        """Word on english, transcript, translation"""

        with open(self.name_file, "a", newline="", encoding="utf8") as f:
            new_row = [word_on_eng, "[" + transcript + "]", translation]

            writer = csv.writer(f)
            writer.writerow(new_row)

    def get_all_word(self):
        """Getter with return of all words of data file"""

        counter = 0
        with open(self.name_file, "r", newline="", encoding="utf8") as f:

            list_length_eng = []
            list_length_trans = []
            for w in csv.reader(f):
                list_length_eng.append(w[0])
                list_length_trans.append(w[1])

            space_after_eng = canculate_max_length(list_length_eng, "ENGLISH")
            space_after_trans = canculate_max_length(list_length_trans, "TRANSCRIPT")

        with open(self.name_file, "r", newline="", encoding="utf8") as f:
            for line in csv.reader(f):

                if counter == 0:
                    print(
                        f'{S_b}{C}    ENGLISH{Bl}{" " * space_after_eng}TRANSCRIPT{G}{" " * space_after_trans}TRANSLATION{W}{S_n}')
                else:
                    text = print_in_row(line, (space_after_eng + 7), (space_after_eng + space_after_trans + 17))
                    print(f'{W}{counter} - {C}{text[0]}{Bl}{text[1]}{G}{text[2]}{W}')

                counter += 1

            if counter == 1:
                print(f'{C}NONE{Bl} \tNONE{G}\t   NONE{W}')

    def remove_row(self, column_number: int):
        """Delete word by index 0-title, 1-word..."""

        counter = 0
        with open(self.name_file, "r", encoding="utf8") as f_data:
            reader = csv.reader(f_data)

            with open("tamp.csv", "w", newline="", encoding="utf8") as f_tamp:
                writer = csv.writer(f_tamp)
                for r in reader:
                    if counter == column_number:
                        counter += 1
                        continue
                    writer.writerow(r)
                    counter += 1

        os.remove(self.name_file)
        os.rename("tamp.csv", self.name_file)

    def clear(self):
        """Clear all word in the data file"""

        with open(self.name_file, "w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writeheader()


def print_in_row(text: list, start_second_word: int, start_last_word: int) -> list:
    """Takes dictionary text
    Integer starts second words (example: "Transcript" ->)"""

    return [text[0] + (" " * (start_second_word - len(text[0]))),
            text[1] + (" " * (start_last_word - (start_second_word + len(text[1])))), text[2]]


def canculate_max_length(text: list, word: str) -> int:
    """Takes list (example: ["Hello", "No", "Okay"])
    Takes word (example: "Transcript")"""

    max_space = 0

    for words in text:
        length_word = len(words)

        if length_word > max_space:
            max_space = length_word

    if max_space - len(word) < 4:
        return 5

    return (max_space - len(word)) + 1


if __name__ == "__main__":
    print(W)

    dictionary = Dictionary("datafiles")

    menu = True
    while menu:
        quation = int(
            input("1 - add word\t2 - get all dictionary\t3 - delete word\n4 - delete all dictionary\nSelect Action: "))

        if quation == 1:
            dictionary.set_word(input("Word on english: ").strip(), input("Transcript: ").strip(),
                                input("Translation: ").strip())
            dictionary.get_all_word()
        if quation == 2:
            dictionary.get_all_word()
        if quation == 3:
            dictionary.get_all_word()
            dictionary.remove_row(int(input("select row: ")))
        if quation == 4:
            dictionary.clear()

        print("\n\n")
