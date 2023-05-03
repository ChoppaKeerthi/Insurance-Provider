import mysql.connector as connector
import datetime as date
import logging
class Admin :
    name = 'INSURANCE PROVIDER'
    dates1 = date.datetime.now()
    admin = 'Keerthi'
    password = 'Keerthi@1303'
    health_insurance = 30000
    accident_insurance = 20000
    death_insurance = 100000
    family_insurance = 50000
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='insurance_provider')

    def showall_user(self):
            query = "select * from user"
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                print("UID  : ", row[0])
                print("Name  : ", row[1])
                print("ADDRESS  : ", row[2])
                print("PHONE  : ", row[3])
                print("DOB  : ", row[4])
                print("INSUANCETYPE   : ", row[5])
                print("INSURANCE_AMOUNT   : ", row[6])
                print()
                print()

    def find_user(self, uid):
        query = "select * from user where uid={}".format(uid)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        if res:
            for row in res:
                print("UID  : ", row[0])
                print("Name  : ", row[1])
                print("ADDRESS  : ", row[2])
                print("PHONE  : ", row[3])
                print("DOB : ", row[4])
                print(" INSURANCE TYPE   : ", row[5])
                print(" INSURANCE AMOUNT  : ", row[6])
                print()
                print()
        else:
            print("USER DOESNT EXIST ! PLEASE TRY WITH VALID USER ")

    def delete_user(self, uid):
        q = "select * from user where uid = {}".format(uid)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            query = "delete from user where uid = {}".format(uid)
            cur = self.con.cursor()
            cur.execute(query)
            res = cur.fetchone()
            self.con.commit()
            print("Your User is Deleted Successfully at  ", self.dates1)
            print()
        else:
            print("USER DOESNT EXIST ! PLEASE TRY WITH VALID USER")

    def update_user(self, uid):
        q = "select * from user where uid = {}".format(uid)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
            newName = input("enter newname : ").capitalize()
            while True:
                newphone = int(input('enter your phone number : '))
                if len(str(newphone)) > 10 or len(str(newphone)) < 10:
                    print("Invalid Phone Number ! Please Enter 10 Digit Only ")
                else:
                    break
            newaddress = input("Enter New Address : ").capitalize()
            query = "update user set uname = '{}' , phone = {} , uaddress = '{}' where uid = {} ".format(
                newName, newphone, newaddress, uid)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Account Details Updated Successfully  at ", self.dates1)
        else:
            print("USER DOESNT EXIST ! PLEASE TRY WITH VALID USER")

    def deleteAlluser(self):
        query = "delete from user"
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print('All User Deleted at ', self.dates1)



