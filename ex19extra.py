#we are defining the function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
# Indentation is very important, it defines where the function ends (not for comments)
    print("Get a blanket.\n")

print("How many cheeses?")
cheese = int(input())
print("Now, how many crackers?")
crackers = int(input())
cheese_and_crackers(cheese, crackers)
