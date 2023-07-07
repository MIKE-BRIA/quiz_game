while True:
    str =input("Enter a word: ")

    if str == str[::-1]:
        print(str,"is palindrome")
    else:
        print(str,"is not palindrome")