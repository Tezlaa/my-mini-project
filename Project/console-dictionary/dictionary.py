import csv
import os


class Dictionary:
    """Name your datas file, default=data"""
    
    def __init__(self, name_file: str="data"):
        
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
        """Getter with return of all words of data file"""
        
        with open(self.name_file, "r", newline="", encoding="utf8") as f:
            for line in csv.reader(f):
                print(line)

            f.close()

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
            f_data.close()
            
            os.remove(self.name_file)
        os.rename("tamp.csv", self.name_file)
                    
    def clear(self):
        """Clear all word in the data file"""
        
        with open(self.name_file, "w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writeheader()

            f.close()

if __name__ == "__main__":
    dictionary = Dictionary("datafiles")
    
    menu = True
    while menu:
        quation = int(input("1 - add word\t2 - get all dictionary\t3 - delete word\n4 - delete all dictionary\nSelect Action: "))
        
        if quation == 1:
            dictionary.set_word(input("Word on english: "), input("Transcript: "), input("Translation: ")) 
            dictionary.get_all_word()
        if quation == 2:
            dictionary.get_all_word()
        if quation == 3:
            dictionary.get_all_word()
            dictionary.remove_row(int(input("select row: ")))
        if quation == 4:
            dictionary.clear()

    