stringA = "This is my string"
stringB = "string my This is"

def checkPermutation(strA, strB):

    strA_len = len(strA)
    strB_len = len(strB)

    # check if strings are the same length
    if(strA_len != strB_len):
        return False

    #creates sorted lists
    a = sorted(strA)
    print(a)
    b = sorted(strB)
    print(b)

    #join lists
    strA = "".join(a)
    print(strA)
    strB = "".join(b)
    print(strB)

    if(strA != strB):
        return false


    return True

if (checkPermutation(stringA, stringB)):
    print("True")
else:
    print("No")
