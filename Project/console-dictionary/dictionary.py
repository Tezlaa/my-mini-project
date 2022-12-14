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
                
                f.close()
    
    def set_word(self, word_on_eng: str, transcript: str, translation: str):
        """Word on english, transcript, translation"""
        
        with open("data.csv", "a", newline="",  encoding="utf8") as f:
            new_row = [word_on_eng, transcript, translation]
            
            writer = csv.writer(f)
            writer.writerow(new_row)
            
            f.close()

    def get_all_word(sefl):
        with open("data.csv", "r", newline="", encoding="utf8") as f:
            for line in csv.reader(f):
                print(line)
            
            f.close()
    
    def clear(self):
        with open("data.csv", "w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writeheader()
            
            f.close() 

if __name__=="__main__":
    dictionary = Dictionary()
    
    #dictionary.set_word("Open", "опэн", "Открыть")
    
    dictionary.get_all_word()
    
    