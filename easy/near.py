def comparison(word1, word2):

    check = 0

    for i in word2:
        
        if i in word1:
            check += 1

    if check == len(word2):
        return True
    else:
        return False


user_word1 = input("Give one word: ")
user_word2 = input("And a second: ")

print(comparison(user_word1, user_word2))
