name = str(input("Name:"))
print("Hello, " + name.strip().title() + "!");

with open("guest_book.txt", 'a') as file:
    file.write(name.strip().title() + "\n")
