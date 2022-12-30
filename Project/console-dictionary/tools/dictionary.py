import csv
import os

from tools.forWords import get_transcript

"""Style """
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
    """Name your data's file, default=data"""

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

    def set_word(self, word_on_eng: str, transcript: str, translation: str) -> None:
        """Word on english, transcript, translation"""

        with open(self.name_file, "a", newline="", encoding="utf8") as f:
            if transcript != "":
                new_row = [word_on_eng.capitalize(), "[" + transcript + "]", translation.capitalize()]
            else:
                new_row = [word_on_eng.capitalize(), transcript, translation.capitalize()]

            writer = csv.writer(f)
            writer.writerow(new_row)

    def get_all_word(self) -> None:
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
                    title = f'    ENGLISH{" " * space_after_eng}TRANSCRIPT{" " * space_after_trans}TRANSLATION'

                    print(
                        f'{"_" * len(title)}\n{S_b}{C}    ENGLISH{Bl}{" " * space_after_eng}TRANSCRIPT{G}'
                        f'{" " * space_after_trans}TRANSLATION{W}{S_n}')
                else:
                    text = print_in_row(line, (space_after_eng + 7), (space_after_eng + space_after_trans + 17))
                    print(f'{W}{counter} - {C}{text[0]}{Bl}{text[1]}{G}{text[2]}{W}')

                counter += 1

            if counter == 1:
                print(f'{C}     NONE{Bl} \t NONE{G}\t\tNONE{W}')

    def edit_row(self, column_number: int) -> None:
        """Edit row by index"""

        counter = 0
        with open(self.name_file, "r", encoding="utf8") as f_data:
            reader = csv.reader(f_data)

            with open("tamp.csv", "w", newline="", encoding="utf8") as f_tamp:
                writer = csv.writer(f_tamp)
                for r in reader:
                    if counter == column_number:
                        os.system('cls||clear')

                        self.get_all_word()

                        word_eng = input(f'\n{paint(" |  EDIT  |", "yel")}\n{paint(" >>>", "cyan")}')
                        r = [word_eng, "[" + get_transcript(word_eng) + "]", input(paint("  >>>", "green"))]
                    writer.writerow(r)
                    counter += 1

        os.remove(self.name_file)
        os.rename("tamp.csv", self.name_file)

    def remove_row(self, column_number: int) -> None:
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

    def clear(self) -> None:
        """Clear all word in the data file"""

        with open(self.name_file, "w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writeheader()


class GameDict(Dictionary):
    pass
    

def print_in_row(text: list, start_second_word: int, start_last_word: int) -> list:
    """

    Args:
        text (list): list -> for text in csv.reader(f)
        start_second_word (int): "Hello" -> second word on 0 index, write 0
        start_last_word (int): "Hello" -> second word on 0 index, write 0

    Returns:
        list: [Hello      ]
    """

    return [text[0] + (" " * (start_second_word - len(text[0]))),
            text[1] + (" " * (start_last_word - (start_second_word + len(text[1])))), text[2]]


def canculate_max_length(text: list, word: str) -> int:
    """
    Args:
        text (list): [Hello, ..., ...]
        word (str): "ENGLISH"

    Returns:
        int: 5...
    """

    max_space = 0

    for words in text:
        length_word = len(words)

        if length_word > max_space:
            max_space = length_word

    if max_space - len(word) < 4:
        return 5

    return (max_space - len(word)) + 1


def paint(text: str, color: str, style: str = "big") -> str:
    """
    Args:
        text  (str) : 'your text'
        color (str) : 'green', 'red', 'yel', 'blue', 'mange', 'cyan'
        style (str) default="big" : 'small'
    
    COLOR: Green='green', Red='red', Yellow='yel', Blue='blue', Magenta='mange', Cyan='cyan', Black/Grey='grey'"""

    available_color = {G: "green", R: "red", Y: "yel", B: "blue", M: "mange", C: "cyan", Bl: "grey"}

    if style == "small":
        style = S_n
    else:
        style = S_b

    for key, value in available_color.items():
        if color == value:
            return f'{style}{key}{text}{W}{S_n}'

    raise ValueError(f'Error, select one from color: {[value for value in available_color.values()]}')
