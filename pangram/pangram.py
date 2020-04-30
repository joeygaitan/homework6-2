# so we want to to find all the characters in the alphabet in the given string.
# Probably want to loop through the least amount of times in the project.
# in my solution I ran up a co

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwyxz"
    alphabet_matrix = {}

    for element in sentence:
        if element.lower() in alphabet:  
            if element.lower() not in alphabet_matrix:                
                alphabet_matrix[element.lower()] = 1

    if len(alphabet_matrix.items()) < 26:
        return False
    else:
        return True

    # for element in sentence:
        
# false condition        
sentence = "abcdefghijklmnopqrstuvwxy"

# true condition
# sentence = "Five quacking Zephyrs jolt my wax bed."

print(is_pangram(sentence))