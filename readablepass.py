import random

wordlist = []
sp_char = ['!','@','#','$','%','&']
num = ['1','2','3','4','5','6','7','8','9','10']

with open('paragraph.txt', 'r') as  file:
    data = file.readlines()

    for lines in data:
        words = lines.split()

        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())

randword = random.choice(wordlist)
randsp_char = random.choice(sp_char)
randnum = random.choice(num)

password = randword + randsp_char + randnum
print(password)

#new comment
