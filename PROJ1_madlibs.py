# string concatentation: connect strings
# suppose we want to create a string that says "madlibs is ___ "

# ways to string concatentate
# adj = fun
# 1) print("maddlibs is " + adj)
# 2) print("maddlibs is {}".format(adj))
# 3) print(f"maddlibs is {fun}}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)