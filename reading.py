print("Welcome to the Reading Tracker!")

while True:
    with open('reader.txt', 'a+') as file1:
        choice = input("Would you like to view the books you have read so far, or enter a new book? (Answer \"new\" for a new book or answer \"view\" to view the books you have read so far!)")
        if choice.lower() == "new":
            book = input("What is the name of the new book you want to put in the tracker?")
            file1.write("\n"+book)
            print("Your book has been succesfully added to reader.txt")
        elif choice.lower() == "view":
            file1.seek(0)
            text = file1.read()
            print(text)
            print("Succesfully printed books from file reader.txt")
        else:
            print("Sorry, that is not a valid answer, please try again!")
