import random

upper = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K']

lower = ['a', 'b', 'c','d','e','f','g','h','i','j','k']

sp_char = ['!','@','#','$','%','&']

num = ['1','2','3','4','5','6','7','8','9','10']

# 4 character password
password = random.choice(upper) + random.choice(lower) + random.choice(sp_char) + random.choice(num)

print(password)
