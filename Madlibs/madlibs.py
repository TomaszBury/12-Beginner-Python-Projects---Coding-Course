# Madlibs
# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ________"

# some string variable
youtuber = "Kylie Ying"

# a few ways to do this:
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"\n Computer programming is so {adj}! \n" + \
    f"It makes me so exlited all the time because I love to {verb1}. \n" + \
    f"Stay hydrated {verb2} like you are {famous_person}.\n\n"

print(madlib)
