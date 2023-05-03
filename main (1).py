from User import User;
from Admin import Admin

import datetime as date

def main() :
    spl_char = ['.', '#''!', '@', '%', '^', '&', '/', '=', '?', '-', '$']
    print()
    print("  WELCOME TO " , Admin.name)
    helpher = User()
    admin = Admin()
    print()
    inp = input("please enter ADMIN or USER :  ")
    if inp == 'user':
        usr = input("please enter 1 for NEW USER  or 2 for EXISTING USER ")
        if usr == '1':

         while True :

          print()
          print("CREATE NEW USER  ")

          try:
            while True:
                try:
                    spl_char = str(['.', '#''!', '@', '%', '^', '&', '/', '=', '?', '-', '$'])
                    name = input('please enter your name : ').capitalize()
                    if spl_char in name:
                        raise TypeError
                    break
                except TypeError as msg:
                    print("special character are not allowed like .., * % # $ @", msg)

            while True:
                phone = int(input('enter your 10 digit  phone number : '))
                if len(str(phone)) > 10 or len(str(phone)) < 10:
                    print("Invalid phone number !Please Try to  enter 10 digit only ")
                else:
                    break
            while True:
                try:
                    DOB = input('please enter your date of birth in DD/MM/YYYY format ')
                    DOB = date.datetime.strptime(DOB, "%d/%m/%y").date()
                    break
                except ValueError:
                    print("Please enter Date of birth in proper format !!! DD/MM/YYYY")

            Address = input('Enter your address : ').capitalize()
            while True:
                print()
                print("Enter the type of Insurance you want to go for : ")
                print("Enter 1 for Health Insurance : ")
                print("Enter 2 for Family Insurance : ")
                print("Enter 3 for Accident Insurance : ")
                print("Enter 4 for Death Insurance : ")
                choice = input("Enter your Insurance Choice : ")
                insurance_amt = 0
                insurance_type = ''
                if choice == '1':
                   insurance_amt = admin.health_insurance
                   insurance_type = 'Health Insurance'.capitalize()
                   break
                elif choice  == '2'  :
                    insurance_amt = admin.family_insurance
                    insurance_type = 'Family Insurance'.capitalize()
                    break
                elif choice =='3':
                    insurance_amt = admin.accident_insurance
                    insurance_type = 'Accident Insurance'.capitalize()
                    break
                elif choice == '4':
                    insurance_amt = admin.death_insurance
                    insurance_type = 'Death Insurance'.capitalize()
                    break
                else:
                    print("Please enter correct Insurance type ")
                    break
            helpher.create(name, Address, phone, DOB,insurance_type,insurance_amt )
            break
          except Exception as e:
            print(e)
            print("INVALID DETAILS ! TRY AGAIN")
        elif usr == '2':
           while True:
             print()
             print("Enter 1 to Display your details  : ")
             print("Enter 2 to Delete your account : ")
             print("Enter 3 to Update  your account : ")
             print('enter 4 to Claim Insurance : ')
             print("Enter 5 to Complete your operations ")
             print()
             try:
              choice = int(input("Enter your choice to perform operations : "))

              if choice == 1:
                uid = int(input("Please enter your account number to fetch your  information : "))
                helpher.find_user(uid)

              elif choice == 2:
                uid = int(input("Please enter an account number to delete your account : "))
                helpher.delete_user(uid)


              elif choice == 3:
                cid = int(input("Please enter account number to update your details : "))
                helpher.update_user(cid)
              elif choice == 4:
                cid = int(input("Please enter account number to claim your insurance : "))
                helpher.claiminsurance(cid)
              elif choice == 5:
                print('Thank you for using ! Welcome back ')
                break
              else:
                print("Invalid input ! try again  ")
             except Exception as e:
               print(e)
               print('Invalid details ! Try again ')

    elif inp == 'admin':
       # while True:
         username = input('Please Enter Username : ')
         password = input('Pleasse Enter Password : ')
         if username != admin.admin and password != admin.password:
            print("Please Enter Correct Credentials ")
            # break
         else:

           while True:
            print()
            print("Enter 1 to display  all users : ")
            print("Enter 2 to display a specific user : ")
            print("Enter 3 to delete an  user : ")
            print("Enter 4 to update  an  user : ")
            print("Enter 5 to delete all users : ")
            print("Enter 6 to complete an transactions : ")
            print()
            try:
                choice = int(input('Please enter your choice to perform operations : '))

                if choice == 1:
                    admin.showall_user()
                elif choice == 2:
                    inp = int(input("Please enter account number to fetch customer details : "))
                    admin.find_user(inp)
                elif choice == 3:
                    inp = int(input("Please enter account number to delete customer  : "))
                    admin.delete_user(inp)
                elif choice == 4:
                    cid = int(input("Please enter account number to update your details "))
                    admin.update_user(cid)
                elif choice == 5:
                    admin.deleteAlluser()
                elif choice == 6:
                    print("Thank you Admin ! See You Soon ")
                    break
                else:
                    print("Invalid input ! Try again ")
            except Exception as e:
                print(e)
                print("Invalid details ! try again ")
    else:
      print("Invalid input please enter user or admin ")

if __name__ == "__main__" :
   main()

