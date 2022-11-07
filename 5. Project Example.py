import random

user = {
   "name": "Tristan",
   "age": random.randint(10, 80)
}

users = []
for _ in range(10):
    users.append(user)
    
print(users)