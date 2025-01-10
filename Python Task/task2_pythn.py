# Fetching the input string from the user
word = input("Please type the word: ")

    
# Plaindrome Function
def is_palindrome(s):
        
    #reverse the string
    reverse_s = s[::-1] # slicing the string by iterating it from the last string

    # condition to check the palindrome
    if s == reverse_s:
        print("The string is a palindrome!")
    else:
        print("The string is not a palindrome!")

is_palindrome(word)