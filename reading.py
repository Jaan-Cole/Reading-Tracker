print("Welcome to the Reading Tracker!")

while True:
    with open('reader.txt', 'a+') as file1:
        choice = input("Would you like to view the books you have read so far, or enter a new book? (Answer \"new\" for a new book or answer \"view\" to view the books you have read so far!)")
        if choice.lower() == "new":
            book = input("What is the name of the new book you want to put in the tracker?")
            file1.write(book+"\n")
            print("Your book has been succesfully added to reader.txt")
        elif choice.lower() == "view":
            count = 0
            while True:
                count += 1
 
                # Get next line from file
                line = file1.readline()
 
                # if line is empty
                # end of file is reached
                if not line:
                    break
                print("Line{}: {}".format(count, line.strip()))
            print("Successfully showed list of books from reader.txt")
        else:
            print("Sorry, that is not a valid answer, please try again!")
