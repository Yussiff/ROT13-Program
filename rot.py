# from string import ascii_lowercase, ascii_uppercase, ascii_letters

def main():
    message = input("Text: ")
    print(f"message: {root(message)}")
    

def root(message):
    alpha = "abcdefghijklmnopqrstuvwxyz" 
    string = ""
    
    for letter in message:
        # Lowercase
        if letter in alpha:
            if alpha.index(letter) < 13:
                string += alpha[alpha.index(letter) + 13]
            else:
                string += alpha[alpha.index(letter) - 13]
        # Uppercase
        elif letter in alpha.upper():
            if alpha.upper().index(letter) < 13:
                string += alpha.upper()[alpha.upper().index(letter) + 13]
            else:
                string += alpha.upper()[alpha.upper().index(letter) - 13]
        # Numbers And Symbols
        else:  # Any Other Conditions/Chars
            string += letter
    return string

main()

