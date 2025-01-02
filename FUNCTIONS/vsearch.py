def search4vowels():
    vowels = set('aeiou')
    word = input('Please enter the word to search for vowels: ')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)

search4vowels()

# Functions Can Accept Arguments
# Rather than having the function prompt the user for a word to search, let’s change
# the search4vowels function so we can pass it the word as input to an argument.

def search4vowels2(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)

search4vowels2('Another word to check for vowels')