import csv
import os


class Dictionary:
    def __init__(self, name_file: str):
        
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

                f.close()

    def set_word(self, word_on_eng: str, transcript: str, translation: str):
        """Word on english, transcript, translation"""

        with open(self.name_file, "a", newline="", encoding="utf8") as f:
            new_row = [word_on_eng, transcript, translation]

            writer = csv.writer(f)
            writer.writerow(new_row)

            f.close()

    def get_all_word(self):
        with open(self.name_file, "r", newline="", encoding="utf8") as f:
            for line in csv.reader(f):
                print(line)

            f.close()

    def remove_row(self, column_number: int):
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
            f_data.close()
            
            os.remove(self.name_file)
        os.rename("tamp.csv", self.name_file)
                    
    def clear(self):
        with open(self.name_file, "w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writeheader()

            f.close()


if __name__ == "__main__":
    dictionary = Dictionary("data")
    
    dictionary.set_word("Open", "опэн", "Открыть") 
    
    dictionary.get_all_word()

    dictionary.clear()
    
    
    