#code to learn list comprehension (Vowel exclusion)
def remove_vowels(word):
    vowels = set('aeiou')
    consonants = [letter for letter in word if letter.lower() not in vowels]
    return consonants

# Sample Input
input_word = str(input())

# Sample Output
output_list = remove_vowels(input_word)
print(output_list)