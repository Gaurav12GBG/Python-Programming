

odd = []
even = []
def evenodd(L):
    for i in L:
        if i % 2 == 0:
            even.append(i)

        else :
            odd.append(i)

    return even, odd

# main function :
L = [12, 4 , 6 , 3 , 7 ,4 , 2 , 5 , 4 , 6 , 3]
even, odd = evenodd(L)
print("Even number list :", even)
print("Odd number list :", odd)

                               # output
                               #
                               #          Even number list : [12, 4, 6, 4, 2, 4, 6]
                               #         Odd number list : [3, 7, 5, 3]
                               #


