import csv
import os

class Dictionary:
    def __init__(self):
        
        #file check
        try:
            os.stat("data.csv").st_size == 0
        except:
            with open("data.csv", "w", newline=""):
                pass
            
        self.header = ["English", "Transcript", "Translation"]
            
        if (os.stat("data.csv").st_size == 0) == True:
            with open("data.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.header)
                writer.writeheader()   
    
    def set_word(self, word_on_eng, transcript, translation):
        with open("data.csv", "r", newline="",  encoding="utf8") as f:
            reader = csv.reader(f)

            with open("data.csv", "w", newline="",  encoding="utf8") as f:
                writer = csv.DictWriter(f, self.header)
                writer.writeheader()
        
                new_row = {"English":word_on_eng,
                        "Transcript": transcript,
                        "Translation":translation,
                        }
                
                for line in reader:
                    writer.writerow(line)
                writer.writerow(new_row)
                    
              
    def get_all_word(sefl):
        with open("data.csv", "r", newline="") as f:
            for line in csv.reader(f):
                print(line)

if __name__=="__main__":
    dictionary = Dictionary()
    
    dictionary.set_word("Opklhsdjfdgd", "опеsdн", "открыdsfть")

    