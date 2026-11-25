# Class List Manager - Group 1
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Ghala (Task 1)
def count_names(names):
    return len(names)
    # Written by: Rawan (Task 2)
def search_name(names, name):
    return name in names


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Number of names:", count_names(names))
print("Search for Sara:", search_name(names, "Sara"))


main()
