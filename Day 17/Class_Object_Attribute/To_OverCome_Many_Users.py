# we use Constructor in python

class User:
    def __init__(self):
        print("New user being Created...")


#object
user_1=User()

#Attribite
user_1.id = "001"
user_1.username = "angele"

print(user_1.username)

"""But we have a of User , then """

user_2 = User()
user_2.id = "002"
user_2.name = "Jack"