# assignment 4
# victor nieto
# vnieto

def encrypt(text, key):
    key = key.upper()
    text = text.upper()
    lk = len(key)
    # will add the resulting characters to result and return result
    result = ""
    # x is place holder to see what letter of the key to add to the text ch.
    x = 1
    # goes through each ch in text and checks if its an upper case letter
    for ch in text:
        if(65 <= ord(ch) <= 90):
            if(len(result) == 8):
                result += " "
            # if ch is an upper case letter and x is length of the key
            # it'll add the last character of key to ch in text and reset x to 1
            if(x == lk):
                t = (ord(ch) - ord('A')) + (ord(key[x-1]) - ord('A'))
                t %= 26
                t += ord('A')
                c = chr(t)
                # adds resulting character to result
                result += c
                x = 1

            # adds current ch from key to ch from text.
            # use mod 26 to wrap back around
            else:
                t = (ord(ch) - ord('A')) + (ord(key[x-1]) - ord('A'))
                t %= 26
                t += ord('A')
                c = chr(t)
                result += c
                x += 1
    return result


def decrypt(text, key):
    key = key.upper()
    text = text.upper()
    lk = len(key)
    # will add the resulting characters to result and return result
    result = ""
    # x is place holder to see what letter of the key to add to the text ch.
    x = 1
    # goes through each ch in text and checks if its an upper case letter
    for ch in text:
        if(65 <= ord(ch) <= 90):
            # if ch is an upper case letter and x is length of the key
            # it'll work with last ch of key
            if(x == lk):
                txtch = (ord(ch) - ord('A'))
                keych = (ord(key[x-1]) - ord('A'))
                # if key ch is greater then the txt ch
                # t has to be the key ch minus the txt
                # character
                if(keych > txtch):
                    t = keych - txtch
                # else you switch the key ch and the txt ch
                # this avoids weird numbers
                else:
                    t = txtch - keych
                t %= 26
                t += ord('A')
                c = chr(t)
                # adds resulting character to result
                result += c
                x = 1

            else:
                txtch = (ord(ch) - ord('A'))
                keych = (ord(key[x-1]) - ord('A'))
                if(keych > txtch):
                    t = keych - txtch
                else:
                    t = txtch - keych
                t %= 26
                t += ord('A')
                c = chr(t)
                result += c
                x += 1
        else:
            # if ch in text is not capital letter then it'll just add the ch
            # without any modification
            result += ch

    return result

def userCrypt():
    msg = input("What is your message? ")
    key = input("What is your key? ")
    crypt = str(input("(E)ncrypt or (D)ecrypt? "))
    crypt = crypt.upper()
    while True:
        print(crypt[0])
        if crypt[0] == 'E':
            result = encrypt(msg, key)
            print("Encrypted message: ", result)
            break
        elif crypt[0] == 'D':
            result = decrypt(msg, key)
            print("Decrypted message: ", result)
            break
        else:
            crypt = str(input("(E)ncrypt or (D)ecrypt? "))
            crypt = crypt.upper()


phrase = "Hello22worl8d"


userCrypt()
