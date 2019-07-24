#Helen Kota 2019
last_letter = 'a'
score = 0
user_word = input("Enter a word starting with " + last_letter)
if user_word.startswith(last_letter):
    score = score+1
    print('score=')
    print(score)
