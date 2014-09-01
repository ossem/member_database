class Frontend():

    def display_root_menu(self):
        print("-------------------------------------")
        print("Welcome to the OSSEM Member Database!")
        print("1) Register new user" )
        print("2) Display user(s)")
        print("Enter 'q' to quit")
        print("-------------------------------------")

    def select_option(self):
        self.display_root_menu()
        selection = input()
        if selection == "1":
            print("Registering new user")
        elif selection == "2":
            print("Displaying users(s)")
        elif selection.lower() == "q":
            print("Exiting program")
        else:
            print("Uh-oh! That wasn't a valid choice.")
        return selection
