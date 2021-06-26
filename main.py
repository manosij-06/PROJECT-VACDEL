from datetime import datetime
from datetime import date
import module_1
import admin_home
import centre_home
import getpass

def fnc_1():
    print("\n\n")
    username = input("\t\t\t   <> Username : ")
    if username.lower() == "esc":
        quit()
    password = getpass.getpass("\n\t\t\t   <> Password : ")
    #password = input("n\t\t\t   <> Password : ")
    module_1.recaptcha()
    check =  module_1.username_password(username,password)
    if check == 1:
        #print("\n\t\t\t\t\t\t------------------------------------------------")
        print("\n\n\n\t\t\t\t\t\t<><><><><>|  Adminstrator {name} login successful      |<><><><><>".format(name = username))
        #print("\t\t\t\t\t\t------------------------------------------------")
        return ("admin",username)
    if check == 2:
        #print("\n\t\t\t\t\t\t-------------------------------")
        print("\n\n\n\t\t\t\t\t\t<><><><><>|  {centre} login successful  |<><><><><>".format(centre=username))
        #print("\t\t\t\t\t\t-------------------------------")
        return ("centre",username)
    else:
        print("\n\t\t\t\t\t\t-------------------------------")
        print("\t\t\t\t\t\t|  Login Failure . Try again  |")
        print("\t\t\t\t\t\t-------------------------------")
        login()

def login():
    role,user = fnc_1()
    if role == "admin":
        print("\n\t\t\t\t\t\t=================================")
        print("\t\t\t\t\t\t|  Adminstrator login homepage  |")
        print("\t\t\t\t\t\t=================================")
        x = admin_home.choice()
        if x == 1 or x is None:
            login()
    elif role == "centre":
        print("\n\t\t\t\t\t\t===========================")
        print("\t\t\t\t\t\t|  Centre login homepage  |")
        print("\t\t\t\t\t\t===========================")
        x = centre_home.choice_2(user)
        if x == 1 or x is None:
            login()


print("\n\n\t\t\t\t               VACCINE CONSIGNMENT SUPPLY PROJECT           ")
print("\n\t\t\t\t                      MAKATHON FINALS 2021           ")

now = datetime.now()
today = date.today()
date = today.strftime("%d %B, %Y")
current_time = now.strftime("%H:%M:%S")
print("\n\t\t\t\t\t  Date : {date}    Time : {current_time}".format(date=date,current_time=current_time))

login()
