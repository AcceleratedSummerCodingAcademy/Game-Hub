#Helen Kota 2019
last_letter = 'a'
score = 0
used_words=[]
while True:
    user_word = input("Enter a word starting with " + last_letter + ': ')
    if not user_word.startswith(last_letter):
        print('Wrong letter! Try again next time!')
        break
    elif user_word in used_words :
        print('You reused a word.Game over!')
        break
    else:
        score = score+1
        print('score=' + str(score) + '!OOT!')
        last_letter = user_word[-1]
        used_words.append(user_word)
    
print('Your High score is ' + str(score) + '!') 
