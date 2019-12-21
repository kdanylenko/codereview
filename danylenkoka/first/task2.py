"""
Обнаружить слова, в которых содержиться цифра 9
"""

my_text = 'I love9 you to the mo9on a9nd back!'

my_text = my_text.split()

index_word = 0
chosen_words = []
join_sign = ", "

while index_word < len(my_text):

    index_character = 0

    while index_character < len(my_text[index_word]):
        if my_text[index_word][index_character] == '9':
            chosen_words.append(my_text[index_word])

        index_character += 1

    index_word += 1

print('Слова, которые подходят:' , join_sign.join(chosen_words))
