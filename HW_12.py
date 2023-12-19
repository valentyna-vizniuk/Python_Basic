# Користувач вводить рядок,
# Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
#     ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
#     підсумкова довжина hashtag має бути не більше 140 символів.
#     кожне слово починається з великої літери.
#     якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# text = str(input('Please enter text: '))
# #text = 'Python Community' # -> #PythonCommunity
# #text= 'i like python community!' # -> #ILikePythonCommunity
# #text = 'Should, I. subscribe? Yes!' # -> #ShouldISubscribeYes

import string
text = input('Type text: ')
text =  text.title().replace(' ', '')
for c in string.punctuation:
    text = text.replace(c, '')
res = f'#{text}'[:140]
print(res)



