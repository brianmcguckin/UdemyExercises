#Check if a book exists in the book collection
collectionOfBooks = ["1984","Brave New World","Slaughterhouse-Five"]
print("Enter book title: ")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Book is in collection")
        break
else:
    print("Book is not in collection")
