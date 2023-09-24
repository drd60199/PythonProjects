print("---Wi-Fi Diagnostic Tree---")

print("Reboot the computer and try to connect.\n(Y/N) Enter Y for yes or N for no.")

user_answer = input("Did that fix the problem? ")

if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
    if user_answer == "y" or user_answer == "Y":
        print("Great! Have a nice day.")
    if user_answer == "n" or user_answer == "N":
        print("Reboot the router and try to connect.")
        user_answer = input("Did that fix the problem? ")

        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
            if user_answer == "y" or user_answer == "Y":
                print("Great! Have a nice day.")
            if user_answer == "n" or user_answer == "N":
                print(" Make sure the cables between the router & modem are plugged in firmly.")
                user_answer = input("Did that fix the problem? ")

                if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                    if user_answer == "y" or user_answer == "Y":
                        print("Great! Have a nice day.")
                    if user_answer == "n" or user_answer == "N":
                        print("Move the router to a new location and try to connect")
                        user_answer = input("Did that fix the problem? ")

                        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                          if user_answer == "y" or user_answer == "Y":
                            print("Great! Have a nice day.")
                          if user_answer == "n" or user_answer == "N":
                             print("Get a new router")