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
    test_list = ['a', 'g', 'f', 'b']
    sorted_list = sort_list(test_list)
    print(test_list)
    print
    print(sorted_list)


test_sort()
