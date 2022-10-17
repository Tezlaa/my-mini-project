
def sequence(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    i = 0
    ialphabet = 0
    inumber = 0
    
    result = []
    
    while i < len(text):
        text2 = text[i]
        try:
            if text2 == alphabet[ialphabet]:
                try:
                    if text[i + 1] == alphabet[ialphabet + 1]:
                        result += text2
                        i += 1
                    elif text[i - 1] == alphabet[ialphabet - 1]:
                        result += text2
                        i += 1
                    else:
                        i += 1
                except:
                    if text[i - 1]  == alphabet[ialphabet - 1]:
                        result += text2
                        i += 1
                    else:
                        i += 1
            elif text2 == number[inumber]:
                try:
                    if text[i + 1] == number[inumber + 1]:
                        result += text2
                        i += 1
                    elif text[i - 1] == number[inumber - 1]:
                        result += text2
                        i += 1
                    else:
                        i += 1
                except:
                    if text[i - 1]  == number[inumber - 1]:
                        result += text2
                        i += 1
                    else:
                        i += 1
            elif text2 == " ":
                i += 1 
            else:
                ialphabet += 1
                inumber += 1
        except:
            if inumber == 10:
                inumber = 0
            else:
                ialphabet = 0
    
    return f'\nThere is a sequence in your text: {result}\n'

print(sequence(input("Write the text you want to check for consistency: ")))
