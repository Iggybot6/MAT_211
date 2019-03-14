def numberate(strIn, convert):
    """
    This function takes a string as an input and returns a list
    of what each character's unicode value is

    "strIn" this is the string that you want to convert

    "convert" is set to True if you want to go from a list of unicode values to a string, and it is set
      to False if you want to go from a string to a list of unicode values.
    """
    strOut = ""  # This string stores each converted charactor
    listOut = []  # This list stores the unicode value of each charactor
    if convert is True:
        for char in range(len(strIn)):
            strOut += chr(strIn[char])
        return strOut
    if convert is False:
        for char in range(len(strIn)):
            listOut.append(ord(strIn[char]))
        return listOut


def stripper(dirtyStr):
    """
    This function strips any non-alphabet(except spaces) characters out of a string
    It returns the string stripped of non-alphabet charactors(except spaces), and a list of the stipped out charactors.
    """
    stripped = ""  # this string is where the stripped string is stored
    stripees = []  # this list is where the stripped out characters are stored
    for char in range(len(dirtyStr)):
        if not (91 <= ord(dirtyStr[char]) <= 96) and (65 <= ord(dirtyStr[char]) <= 122 or ord(dirtyStr[char]) == 32):
            stripped += dirtyStr[char]
        else:
            stripees += dirtyStr[char]
    return stripped # the return for stripees was removed as it is not needed in this application.


def caseChanger(strIn, caps):
    """
    This function converts the case of all of the charactors in a string to either upper or lowercase.

    "strIn" is the string you want to convert
    "caps" is set to true to make the string capital, and false to make the string lowercase

    The function returns a string all in the same case.
    """
    strOut = ""  # This string is where the coverted string is stored
    for char in range(len(strIn)):
        if caps is True:  # This converts to uppercase
            if ord(strIn[char]) > 96:
                strOut += chr((ord(strIn[char]) - 32))
            else:
                strOut += strIn[char]
        if caps is False:  # This converts to lowercase
            if ord(strIn[char]) < 96 and ord(strIn[char]) != 32:
                strOut += chr((ord(strIn[char]) + 32))
            else:
                strOut += strIn[char]
    return strOut


def alphabatizer(listIn, convert):
    """
    This function takes a list of unicode values and turns them into thier position in the alphabet,
    with a being 1 and z being 26. A space is stored as 32

    This function expects the list of unicode values to be for lowercase charactors.

    "convert" is set to True if you want to go from a list of 0-25 to a list of lowercase unicode values,
      and it is set to False if you want to go from a list of lowercase unicode values to a list of 0-25
    """
    listOut = []  # This list stores the converted values
    if convert is True:
        for index in range(len(listIn)):
            if listIn[index] == 32:
                listOut.append(listIn[index])
            else:
                listOut.append(listIn[index] + 97)
    if convert is False:
        for index in range(len(listIn)):
            if listIn[index] == 32:
                listOut.append(listIn[index])
            else:
                listOut.append(listIn[index] - 97)
    return listOut


def encode(strIn, startLtr, decode):
    """
    This function encodes a message with a ceaser chiper.

    "decode" is set to true if you want to decode the message
    """

    listOut = []
    keyLetter = ord(caseChanger(startLtr, False)) - 97  # This process makes startLtr something that we can work with
    messageIn = alphabatizer(numberate(caseChanger(stripper(strIn), False), False), False)  # This processes strIn to make it work well with this function
    if decode is True:
        for char in range(len(messageIn)):
            if messageIn[char] == 32:
                listOut.append(messageIn[char])
            else:
                listOut.append(((messageIn[char] - keyLetter) % 26))
    if decode is False:
        for char in range(len(messageIn)):
            if messageIn[char] == 32:
                listOut.append(messageIn[char])
            else:
                listOut.append(((messageIn[char] + keyLetter) % 26))
    strOut = numberate(alphabatizer(listOut, True), True)
    return strOut


def keyworder(strIn, keyIn, decode):
    """
    this function will iterate over the encode function in order to encrypt the string based off of the
    each charactor in the key word.
    """
    strOut = strIn
    for char in range(len(keyIn)):
        strOut = encode(strOut, keyIn[char], decode)
        # print(strOut)
        # print("")
    return strOut


# Main Body
myStr = input("Type in your string here:")
myJob = bool(input("Type in true if you want to Decode the string, or type in false if you want to Encode the string "))
cipherStart = input("Where do you want to start the cipher?")
otherStr = keyworder(myStr, cipherStart, myJob)
print(otherStr)
# print(keyworder(otherStr, cipherStart, True))
