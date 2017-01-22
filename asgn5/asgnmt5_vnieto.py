# assignment 5
# victor nieto
# vnieto
import os.path
def open_file(filename):
    # opens input file
    f = open(filename, 'r')
    # f_string is a list of words in the input file
    f_string = f.read().strip().split()
    return f_string

def clean_list(word_list):
    result = []
    for word in word_list:
        clean_word = ''
        for ch in word:
            if ch.isalnum():
                clean_word += ch
            elif ch.isspace():
                clean_word += ch
        result.append(clean_word.lower())
    return result

def test_clean_list():
    test = ['hello!', '21savage', 'my$man', 'fu%* that']
    print(test)
    clean_test = clean_list(test)
    print(clean_test)

def sort_list(to_sort):
    # copy passed to_sort list into A
    A = to_sort[:]
    B = []
    # variables to keep track of which list you're on
    this = "A"
    other = "B"
    A.append(False)
    B.append(False)
    prev = 'z'*100
    while True:
        a = A[0]
        b = B[0]
        # if a and b are false
        if (a == False) and (b == False):
            # if A is 'empty' then return B starting at index one
            # to remove boolean value
            if(len(A) == 1):
                return B[1:]
            # vice versa
            elif(len(B) == 1):
                return A[1:]
            # if none of the lists are 'empty' remove false boolean
            # value from top and append them to the end of the list
            # sets previous to 100 x 'z' also
            else:
                temp1 = A.pop(0)
                temp2 = B.pop(0)
                A.append(temp1)
                B.append(temp2)
                prev = 'z'*100
        else:
            # if a is false choose value at top of B
            if a == False:
                next = B.pop(0)
                # appends next to correct list

                # if next comes before prev
                # append next to current list
                if next >= prev:
                    if this == 'A':
                        A.append(next)
                        prev = next
                    else:
                        B.append(next)
                        prev = next
                # if next comes after prev
                # append next to end of other list
                # make this list equal to other list
                # and other list equal to this list(swap)
                else:
                    if other == 'B':
                        B.append(next)
                        prev = next
                        this = 'B'
                        other = 'A'
                    else:
                        A.append(next)
                        prev = next
                        this = 'A'
                        other = 'B'
            # if b is false and a isnt then choose value at top of A
            elif b == False:
                next = A.pop(0)
                # appends next to correct list

                # if next comes before prev
                # append next to current list
                if next >= prev:
                    if this == 'A':
                        A.append(next)
                        prev = next
                    else:
                        B.append(next)
                        prev = next
                # if next comes after prev
                # append next to end of other list
                # make this list equal to other list
                # and other list equal to this list(swap)
                else:
                    if other == 'B':
                        B.append(next)
                        prev = next
                        this = 'B'
                        other = 'A'
                    else:
                        A.append(next)
                        prev = next
                        this = 'A'
                        other = 'B'
            # if a comes before prev and b doesnt then choose value at top of A
            elif (a >= prev) and (b < prev):
                next = A.pop(0)
                # appends next to correct list

                # if next comes before prev
                # append next to current list
                if next >= prev:
                    if this == 'A':
                        A.append(next)
                        prev = next
                    else:
                        B.append(next)
                        prev = next
                # if next comes after prev
                # append next to end of other list
                # make this list equal to other list
                # and other list equal to this list(swap)
                else:
                    if other == 'B':
                        B.append(next)
                        prev = next
                        this = 'B'
                        other = 'A'
                    else:
                        A.append(next)
                        prev = next
                        this = 'A'
                        other = 'B'
            # if b comes before prev and a doesn't then choose value at top of B
            elif (b >= prev) and (a < prev):
                next = B.pop(0)
                # appends next to correct list

                # if next comes before prev
                # append next to current list
                if next >= prev:
                    if this == 'A':
                        A.append(next)
                        prev = next
                    else:
                        B.append(next)
                        prev = next
                # if next comes after prev
                # append next to end of other list
                # make this list equal to other list
                # and other list equal to this list(swap)
                else:
                    if other == 'B':
                        B.append(next)
                        prev = next
                        this = 'B'
                        other = 'A'
                    else:
                        A.append(next)
                        prev = next
                        this = 'A'
                        other = 'B'
            # if both values a and b come before previous alphabetically then choose the value that
            # comes after the other
            else:

                if b > a:
                    # a comes after b
                    next = A.pop(0)
                    # appends next to correct list

                    # if next comes before prev
                    # append next to current list
                    if next >= prev:
                        if this == 'A':
                            A.append(next)
                            prev = next
                        else:
                            B.append(next)
                            prev = next
                    # if next comes after prev
                    # append next to end of other list
                    # make this list equal to other list
                    # and other list equal to this list(swap)
                    else:
                        if other == 'B':
                            B.append(next)
                            prev = next
                            this = 'B'
                            other = 'A'
                        else:
                            A.append(next)
                            prev = next
                            this = 'A'
                            other = 'B'
                else:
                    next = B.pop(0)
                    # appends next to correct list

                    # if next comes before prev
                    # append next to current list
                    if next >= prev:
                        if this == 'A':
                            A.append(next)
                            prev = next
                        else:
                            B.append(next)
                            prev = next
                    # if next comes after prev
                    # append next to end of other list
                    # make this list equal to other list
                    # and other list equal to this list(swap)
                    else:
                        if other == 'B':
                            B.append(next)
                            prev = next
                            this = 'B'
                            other = 'A'
                        else:
                            A.append(next)
                            prev = next
                            this = 'A'
                            other = 'B'

def test_sort():
    test = ['h', 's', 't', 'a', 'c']
    print(test)
    print()
    sorted_test = sort_list(test)
    print(sorted_test)

def print_count(sorted_list):
    # place holder for previous word
    prev = ""
    count = 1
    for word in sorted_list:
        # first time around make previous the current word
        if prev is None:
            prev = word
        # if current word is same as previous then increment count
        elif word == prev:
            count += 1
        # if current word is different than previous word, print
        # the previous word and its count before changing those
        # values for the next run
        else:
            print(str(count) + " " + prev)
            count = 1
            prev = word
    print(str(count) + " " + prev)

# test_clean_list()
# test_sort()

# sorted_file = sort_list(f_string)
# print_count(sorted_file)

def main():
    filename = input("enter name of file you want to open: ")
    while True:
        if os.path.isfile(filename):
            break
        else:
            print("unable to open file")
            filename = input("enter name of file you want to open: ")
    f_string = open_file(filename)
    f_string = clean_list(f_string)
    sorted_file = sort_list(f_string)
    print_count(sorted_file)

main()
