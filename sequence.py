alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def sequence(text):
    i = 0
    ialphabet = 0
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
            elif text2 == " ":
                i += 1 
            else:
                ialphabet += 1
        except:
            ialphabet = 0
    return result        
    

print(sequence(input("Write the text you want to check for consistency: ")))
