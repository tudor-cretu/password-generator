import random
import string
import pandas as pd

generate = True
while generate is True:
    generate = str.lower(input("Do you want to generate a pasword?: "))
    if generate == "yes":
        generate = True
    elif generate == "no":
        print("You quit the program.")
        quit()
    else:
        generate = str.lower(input("Please choose between 'yes' or 'no': "))
        if generate == 'yes':
            generate = True
        elif generate == 'no':
            print("You quit the program.")
            quit()
        else:
            print("Please choose a valid option (yes or no).")
            print("The program quit.")
            continue
    if generate == True:
        platform = input("Enter your desired platform (type 'no' if you don't want to specify it): ")
        username = input("Enter your desired username: ")
        length = 20 # number of characters in the password
        total = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(total, length))
        if str.lower(platform) != 'no':
            print("Platform: " + platform)
        print("Username: " + username)
        print("Password: " + password)

    df = pd.DataFrame({'Platform': [platform],
                      'Username': [username],
                      'Password': [password]})
    print(df)
    df.to_excel(r'F:\Programming\Python\Pycharm Projects\platforms_usernames_passwords.xlsx', index=False, header = True)

