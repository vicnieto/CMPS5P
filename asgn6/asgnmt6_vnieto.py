# assignment 6
# Victor Nieto
# vnieto
from asgn5 import asgnmt5_vnieto
import os.path

def files():
    while True:
        list_files = []
        file_name = input("Enter name of file you want to open (enter blank if you have no more files): ")
        while True:
            if file_name == "":
                break
            elif(os.path.isfile(file_name)):
                list_files.append(file_name)
                file_name = input("Enter name of file you want to open (enter blank if you have no more files): ")

            else:
                print("File name you entered can't be opened. Try again")
                file_name = input("Enter name of file you want to open (enter blank if you have no more files): ")
        return list_files

def test_files():
    file_list = files()
    print(file_list)

# test_files()

def clean_list(fileobj):
    # grabs file object and reads in the text, strips blanks from beginning
    # and end, converts all letters to lower case, and splits the string
    # into a list of strings or list of words
    fobj = open(fileobj, encoding='utf8')
    word_list = fobj.read().strip().lower().split()
    result = []
    for word in word_list:
        clean_word = ''
        for ch in word:
            if ch.isalpha():
                clean_word += ch
            elif ch.isspace():
                clean_word += ch
        result.append(clean_word)
    return result

def word_count(word_list):
    word_dict = {}
    # goes through each word in given word list
    for word in word_list:
        # if the word is in the list of keys in the dictionary given
        # it'll add 1 to the value of the word key because the word
        # has shown up more than once
        if word in word_dict:
            word_dict[word] += 1
        # if the word isn't a key, it makes it a key and sets its
        # value as 1
        else:
            word_dict[word] = 1
    return word_dict

def letter_count(word_list):
    # empty dictionary where letter keys will be added
    letter_dict = {}
    # goes through each word in given list
    for word in word_list:
        # goes through each ch in word
        for ch in word:
            # if the ch is a key in letter dictionary it adds 1 to its value
            # because the ch shows up more than once
            if ch in letter_dict:
                letter_dict[ch] += 1
            # if it is the first time the ch is seen, it adds the ch to list
            # of keys and sets its value to 1
            else:
                letter_dict[ch] = 1
    return letter_dict

def test_lettercount():
    test = "the quick brown fox jumped over the brown dog"
    test = test.split()
    letter_dict = letter_count(test)
    print(letter_dict)


def count_window(word_list, window):
    # empty dictionary where bigrams and trigrams will be added
    count_dict = {}
    # empty string where ch's from words will be added
    temp = ""
    # goes throug heach word in Word list given
    for word in word_list:
        # last_index = len(word) - 1
        # iterates i from 0 to length of word - 1
        for i in range(len(word)):
            if len(word) < window:
                break
            # if i + the window is the length of the word we are analyzing
            # this is the last substring of length window we want to get from
            # this word
            if i + window == len(word):
                # sets temp equal to a substring of word
                # substring is of length window
                temp = word[i : i + window]
                # if the string temp is a key in count_dic dictionary
                # it will add 1 to its value because its a trigram or
                # bigram that we've seen before
                if temp in count_dict:
                    count_dict[temp] += 1
                # if temp is not a key, we set its value equal to 1 in
                # count_dic dictionary
                else:
                    count_dict[temp] = 1
                # breaks out of for loop to stop unnecessary creation of substrings
                break
            # does the same thing as above but doesn't break out of the loop
            # because we aren't at the last substring yet
            else:
                temp = word[i: i + window]
                if temp in count_dict:
                    count_dict[temp] += 1
                else:
                    count_dict[temp] = 1
    return count_dict

def test_countdic():
    test = "the quick brown fox jumps over the boy's lazy dog"
    test = test.split()
    countwindow_dict = {}
    countwindow_dict = count_window(test, 2)
    print(countwindow_dict)

def test_wordcount():
    test = "the quick brown fox jumped over the brown dog"
    test = test.split()
    test_dict = word_count(test)
    print(test_dict)

def dict_total(dict):
    count = 0.0
    for key in dict:
        count += dict[key]
    return count


def format_print(type, dict):
    print(type)
    for i in sorted(dict, key=dict.get, reverse=True)[:25]:
        percent = float(dict[i] / dict_total(dict)) * 100
        print("{0:<11} : {1:<5} ({2:.3f}%)".format(i, dict[i], percent))


def test_formatprint():
    type = "Letter frequencies"
    test = "the quick brown fox jumped over the brown dog"
    test = test.split()
    test_dict = count_window(test, 3)
    format_print(type, test_dict)

# test_formatprint()
# test_countdic()
# test_lettercount()
# test_wordcount()
# JSawyers main function. Might be helpful later.

# for y in sorted(dictionary, key=dictionary.get, reverse=True)[:25]

# def main():
#     files = interface()
#     stats = {}
#     for filepath in files:
#        read_and_cleansed = preprocess_book_content()

def main():
    # files returns list of files user wants to open and stores it in file_list
    file_list = files()
    # empty dictionary where stats for each file will be stored
    stats = {}
    # empty list to store total words in all files
    total_word_list = []
    # for each file in file_list
    for filepath in file_list:
        # refines file object into a list of lower case words with no punctuation
        word_list = clean_list(filepath)
        # adds this list to the list of all words
        total_word_list += word_list
        stats[filepath] = {}
        # adds dictionaries for letters, words, bigrams, and trigrams to the key named after
        # the file its analyzing
        stats[filepath]['letters'] = count_window(word_list, 1)
        stats[filepath]['words'] = word_count(word_list)
        stats[filepath]['bigrams'] = count_window(word_list, 2)
        stats[filepath]['trigrams'] = count_window(word_list, 3)
        # begins printing statistics for each file with specific format
        print("---- Statistics for file {0:<8}".format(filepath))
        print()
        format_print("Letter frequencies", stats[filepath]['letters'])
        print()
        format_print("words", stats[filepath]['words'])
        print()
        format_print("bigrams", stats[filepath]['bigrams'])
        print()
        format_print("trigrams", stats[filepath]['trigrams'])
        print()
    # adds dictionaries to stats['total'] key with letters, words, bigrams, etc.
    # like I did above, but this time for a list with total words from all files
    stats['total'] = {}
    stats['total']['letters'] = count_window(total_word_list, 1)
    stats['total']['words'] = word_count(total_word_list)
    stats['total']['bigrams'] = count_window(total_word_list, 2)
    stats['total']['trigrams'] = count_window(total_word_list, 3)
    # prints formatted overall statistics
    print("---- Overall Statistics")
    print()
    format_print("Letter frequencies", stats['total']['letters'])
    print()
    format_print("words", stats['total']['words'])
    print()
    format_print("bigrams", stats['total']['bigrams'])
    print()
    format_print("trigrams", stats['total']['trigrams'])

main()
