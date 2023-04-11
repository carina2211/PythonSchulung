# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
first_name = "Carina"  # string
last_name = "Reichwein"  # string
age = 32  # int
y = 10.09  # fload
z = 10.09  # fload
# aninmal_list = ["Amsel", "Drossel", "Fink", "Star", "Ente", ["Giraffe", "Elefant"]]
# aninmal_list_sorted = sorted(aninmal_list)

backwaren = []
print(backwaren)
backwaren.append("Kekse")
backwaren.append("Kuchen")
backwaren.append("Salzstange")

print(backwaren)

backwaren.pop(-1)
print(backwaren)

backwaren.insert(1,"Brot")

print(backwaren.index("Kuchen"))

print(backwaren[-1])

backwaren.sort()
print (backwaren)
# print(aninmal_list["Amsel"][1])


# print(f"Original: {aninmal_list}")
# print(f"Sortiert: {aninmal_list_sorted}")
# print(f"Anzahl: {len(aninmal_list)}")

# aninmal_list.append("Gans")
# print(f"Original: {aninmal_list}")

# print(f"Anzahl: {len(aninmal_list)}")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
