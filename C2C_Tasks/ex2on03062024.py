string1 = input("Enter the string you want to check palindrome: ")


def palindrome(string1):
    string1 = string1.lower()
    string2 = string1[::-1]
    if string1 == string2:
        print("The given string is palindrome")
    else:
        print("The given string is not a palindrome")


palindrome(string1)
