
import datetime as datetime
import mysql.connector
import datetime as date
date1 = datetime.datetime.now()



SpecialSym = ['$', '@', '#', '%']



mydb = mysql.connector.connect(host="127.0.0.1", user='root', password='AmmuRam.16', database='Bank_Database')
mycur = mydb.cursor()
#created the bank table
mycur.execute(
    "create table if not exists Bank(account_no BIGINT(255) primary key, first_name varchar(30), last_name varchar(30), user_name varchar(30), password tinytext, date_of_birth date, address varchar(40), mobile_No varchar(30), aadhaar_No varchar(30), balance int)")
# Created the Transaction Table
mycur.execute(
    "create table if not exists Transaction(user_name varchar(20), credited int, debited int,date1 datetime)")



while True:
    print('\n')
    print('---------------------------------------------------')
    print('************ WELCOME TO EDFX BANK OF INDIA **********')
    print('---------------------------------------------------')
    print('Press 1 to Sign Up')
    print('Press 2 to Sign in')
    print('Press 3 to Admin Login')
    print('Press 4 to EXIT')
    ch = int(input("Enter Your choice Here: "))
    try:
        if (ch >= 5):
            raise Exception("oops!!..That was not valid number..try again")
        elif ch == 1:
            while True:
                try:
                    a1 = '@'
                    a2 = '#'
                    a3 = '$'
                    a4= '%'
                    a5='&'
                    a6= '*'
                    a7='-'
                    a8='?'
                    f_name = input("Enter Your First Name Here: ")

                    if (a1 in f_name) or (a2 in f_name) or (a3 in f_name) or (a4 in f_name) or (a5 in f_name) or (a6 in f_name) or (a7 in f_name) or (a8 in f_name):
                        raise TypeError
                    break
                except TypeError:
                    print("Special characters not allowd")

            while True:
                try:
                    a1 = '@'
                    a2 = '#'
                    a3 = '$'
                    a4 = '%'
                    a5 = '&'
                    a6 = '*'
                    a7 = '-'
                    a8 = '?'

                    l_name = input("Enter Your last Name Here : ")
                    if (a1 in l_name) or (a2 in l_name) or (a3 in l_name) or (a4 in l_name) or (a5 in l_name) or (a6 in l_name) or (a7 in l_name) or (a8 in l_name):
                        raise TypeError
                    break
                except TypeError:
                    print("Special characters not allowed")

            while True:
                try:
                    a1 = '@'
                    a2 = '#'
                    a3 = '$'
                    a4 = '%'
                    a5 = '&'
                    a6 = '*'
                    a7 = '-'
                    a8 = '?'

                    UserName = input("Enter Your User Name Here: ")
                    if (a1 in UserName) or (a2 in UserName) or (a3 in UserName) or (a4 in UserName) or (a5 in UserName) or (a6 in UserName) or (a7 in UserName) or (a8 in UserName) :
                        raise TypeError
                    break
                except TypeError:
                    print("Special Characters not allowed")

            while True:
                try:
                    password = input("Enter Your Password Here: ")
                    if len(password) < 6:
                        raise ValueError("Password should contain at least 6 characters")
                    if not any(char.isdigit() for char in password):
                        raise ValueError("Password should contain at least 1 number")
                    if not any(char.isupper() for char in password):
                        raise KeyError("Password should contain at least 1 upper case character")
                    if not any(char.islower() for char in password):
                        raise KeyError("Password should contain at least 1 lower case character")
                    if not any(char in SpecialSym for char in password):
                        raise KeyError
                    break
                except ValueError:
                    print(
                        "password should contain at least 1 upeer case, 1 lower case, 1 special character and password should contain 7 characters")
                except KeyError:
                    print(
                        "password should contain at least 1 upeer case, 1 lower case, 1 special character and password should contain 7 characters")

            while True:
                try:
                    Date_of_birth = input("Enter Your Date of Birth in given format DD/MM/YYYY : ")
                    Date_of_birth = date.datetime.strptime(Date_of_birth, "%d/%m/%Y").date()
                    break
                except ValueError:
                    print("Please enter your date of birth in given format !!! DD/MM/YYYY")

            Balance = input("Enter Amount of money That you want to deposit: ")
            address = input("Enter Your Address Here: ")

            while True:
                try:
                    Mobile_Number = (input("Enter Your 10 digit Mobile Number Here: "))
                    if len(Mobile_Number) != 10:
                        raise ValueError("Please enter valid 10 digit mobile number")
                    break
                except ValueError as m:
                    print(m)

            unique_code = 16
            Account_no = int(str(unique_code) + Mobile_Number)

            while True:
                try:
                    Aadhar_no = input("Enter Your Aadhar number Here: ")
                    if len(Aadhar_no) != 12:
                        raise ValueError("Please Enter Your 12 digit Aadhar Number ")
                    break
                except ValueError as m:
                    print(m)

            sql = f"insert into bank VALUES ({Account_no},'{f_name}','{l_name}','{UserName}','{password}','{Date_of_birth}','{address}','{Mobile_Number}','{Aadhar_no}','{Balance}')"
            mycur.execute(sql)
            mydb.commit()
            print(("\n"))
            print("--------------------------------------------------------------------------")
            print("*********** Dear " f'{f_name}'", Your Account.no is", f'{Account_no}', 'and ****************')
            print("*********** Account Has Been Created Successfully Kindly Login ************")
            print("------------------------------------------------------------------------------")
            # break

            # while True:
        if ch == 2:
            User_Name = input("Enter Your User Name Here: ")
            password = input("Enter Your Password: ")
            rp = "select * from bank where User_Name ='{}' and Password ='{}'".format(User_Name, password)
            mycur.execute(rp)
            data = mycur.fetchall()
            if data:
                while True:
                    print("\n")
                    print("--------------------------------------------------------")
                    print("************ Welcome to EDFX Bank Of India ************")
                    print("--------------------------------------------------------")
                    print("Welcome ",data[0][1])
                    print("\n")
                    print("Press 1 To Withdraw money")
                    print("Press 2 To Deposit money")
                    print("Press 3 To view the last 5 Transaction ")
                    print("Press 4 To View Your Profile")
                    print("Press 5 TO Update Account Details")
                    print("Press 6 To Delete Your Account Permanently")
                    print("press 7 To Log Out")
                    ch1 = int(input("Enter Your choice Here: "))
                    print("-------------------------------------")

                    try:

                        if (ch1>=8):
                            raise TypeError("")
                    except TypeError:
                        print("oops!! that was an invalid input")

                    balance=0
                    if ch1==1:
                        try:
                            rb="select Balance from bank where User_Name='{}'".format(User_Name)
                            mycur.execute(rb)
                            balance=mycur.fetchone()[0]
                        except:
                            print("oops")
                        print("\n")
                        print("---------------------------------")
                        print("Your Account Balance is:", balance)
                        print("----------------------------------")
                        while True:
                            try:
                                print("-----------------------------------------------")
                                debited = int(input("Enter the Amount of withdrawl: "))
                                print("------------------------------------------------")
                            except :
                                print("oops!! that was an invalid input")
                                continue

                            if debited <= balance:
                                credited = 0

                                st = "update bank set Balance=GREATEST(0,Balance - '{}') where User_Name='{}'".format(debited,User_Name)
                                mycur.execute(st)
                                mydb.commit()


                                sql1=f"insert into Transaction values('{User_Name}',{credited},{debited},'{date1}')"
                                mycur.execute(sql1)
                                mydb.commit()

                                rs="select Balance from bank where User_Name='{}'".format(User_Name)
                                mycur.execute(rs)
                                bal1=mycur.fetchone()[0]
                                print("\n")
                                print("----------------------------------------------------------------------")
                                print(" Your UserName ",User_Name,"is debited with Rs", debited,"on",date1)
                                print("-----towards NetBanking.Available Balance is Rs.",bal1,"only ---------")
                                print("----------------------------------------------------------------------")
                                print("\n")
                            elif debited>balance:
                                    print("------------------------------------------------------------------")
                                    print("******* OOPS !! insufficient balance please try again! ********")
                                    print("-------------------------------------------------------------------")
                            break
                    elif ch1==2:
                        Debited=0

                        while True:
                            try:
                                print("\n")
                                print("--------------------------------------------------")
                                deposit = (input("Enter the Amount You want to Deposit: "))
                                print("--------------------------------------------------")
                                if deposit.isalpha():
                                    print("oops!! that was an invalid input")
                                else:

                                    sqt="update bank set Balance=Balance +'{}' where User_Name='{}'".format(deposit,User_Name)
                                    mycur.execute(sqt)
                                    mydb.commit()

                                    sql2="insert into Transaction values('{}',{},{},'{}')".format(User_Name,deposit,Debited,date1)
                                    mycur.execute(sql2)
                                    mydb.commit()

                                    rs2="select Balance from bank where User_Name='{}'".format(User_Name)
                                    # print(rs2)
                                    mycur.execute(rs2)
                                    bal2=mycur.fetchone()[0]
                                    print("\n")
                                    print("------------------------------------------------------------------------------")
                                    print("-----Your User Name",User_Name,"is credited with Rs",deposit,"on",date1,"-----")
                                    print("---------towards Net Banking. Avialable Balance is Rs : ", bal2,"only---------")
                                    print("------------------------------------------------------------------------------")
                                    break
                            except TypeError:
                                print("oops")
                    elif ch1==3:
                        transact="select Credited, Debited , date1 from transaction where User_Name='{}' limit 5".format(User_Name)
                        mycur.execute(transact)
                        print("\n")
                        print("*******Transaction Details are as follows *********")
                        for i in mycur:
                            print("----------------------------------------------")
                            print("Credited,Debited : ", i)
                            print("----------------------------------------------")

                    elif ch1==4:
                        view_profile=f"select * from bank where User_Name='{User_Name}'"
                        mycur.execute(view_profile)
                        res=mycur.fetchall()
                        print("------------------------------------------")
                        print("************ ACCOUNT DETAILS *************")
                        print("------------------------------------------")
                        print("----------------------------------------------------------------------")
                        for item in res:
                            print(f"Account Number is: ",item[0])
                            name=f'{item[1]}'+''+f'{item[2]}'
                            print(f"Account Holder's Name: ",name)
                            print(f"User Name of the Account Holder's:",item[3])
                            print(f"Password of the Account Holder's:",item[4])
                            print(f"Date of Birth of the Account Holder's:",item[5])
                            print(f"Address of the Account Holder's:",item[6])
                            print(f"Mobile Number of the Account Holder's:",item[7])
                            print(f"Aadhar Number of the Account Holder's:",item[8])
                            print(f"Balance of the Account Holder's:",item[9])

                    elif ch1==5:
                        while True:
                            print("\n")
                            print("---------------------------------------------------------")
                            print('*************** ACCOUNT SETTINGS ************************')
                            print("---------------------------------------------------------")
                            print("Welcome",data[0][1])
                            print("\nPress 1 To Update Your Name:")
                            print("Press 2 To Update Your User Name: ")
                            print("Press 3 To update Your Password: ")
                            print("Press 4 To Update Your Mobile Number: ")
                            print("Press 5 To Update Your Address: ")
                            ch2=int(input("Enter Your Choice is Here: "))
                            try:
                                if ch2>=6 :
                                    print("error")
                            except:
                                print("----------------------------------")
                                print("oops!!! that was an invalid input")
                                print("----------------------------------")
                                continue
                            break
                        if ch2==1:
                            try:
                                update_first_name=input("Enter Your First Name Here: ")
                                update_last_name=input("Enter Your Last Name Here: ")
                                sql_update_name="update bank set First_Name='{}', Last_Name='{}'  where User_Name='{}'".format(update_first_name,update_last_name,User_Name)
                                mycur.execute(sql_update_name)
                                mydb.commit()
                                print("-----------------------------------------------")
                                print("****** Your Name is Updated Successfully ******")
                                print("------------------------------------------------")
                            except:
                                print("error")
                        if ch2==2:
                            try:
                                update_user_name=input("Enter Your User Name Here: ")
                                sql_upadte_u_name="update bank set User_Name='{}' where Password='{}'".format(update_user_name,password)
                                mycur.execute(sql_upadte_u_name)
                                mydb.commit()
                                print("----------------------------------------------------")
                                print("****** Your User Name is Updated Successfully ******")
                                print("----------------------------------------------------")
                            except:
                                print("error")

                        elif ch2 == 3:
                            try:
                                Update_NewPassword = input("Enter Your New Password: ")
                                sql_Update_New_Password = "update bank set Password='{}' where User_Name='{}'".format(
                                    Update_NewPassword, User_Name)
                                mycur.execute(sql_Update_New_Password)
                                mydb.commit()
                                print("Password is Updated Successfully")
                            except:
                                print("Error")

                        elif ch2 == 4:
                            while True:
                                try:
                                    Update_mobile_no = (input("Enter Your Mobile Number : "))
                                    if (len(Update_mobile_no) != 10) or Update_mobile_no.isalpha():
                                        print("Error")
                                    sql_Update_mobile_no = "update bank set Mobile_No='{}' where  User_Name='{}'".format(
                                        Update_mobile_no, User_Name)
                                    mycur.execute(sql_Update_mobile_no)
                                    mydb.commit()
                                    print("_________________________________________________________________________")
                                    print("   ***** Your Mobile Number is Updated Successfully *****   ) ")
                                    print("_________________________________________________________________________")
                                except IndexError:
                                    print("________________________________________________________")
                                    print("**** Please Enter a valid 10 digit Mobile Number ******")
                                    print("________________________________________________________")
                                    continue
                                break

                        elif ch2 == 5:
                            try:
                                Update_Address = input("Enter Your Address Here: ")
                                sql_Update_Address = "update bank set Address='{}' where User_Name='{}'".format(
                                    Update_Address, User_Name)
                                mycur.execute(sql_Update_Address)
                                mydb.commit()
                                print("_________________________________________________________________________")
                                print("   *** Address is Updated Successfully ***  :) ")
                                print("_________________________________________________________________________")
                            except :
                                print("Error")

                    elif ch1 == 6:
                        acc_no=input("Enter Your Account Number: ")
                        sql_Delete_ACC = f"delete from bank where Account_no={int(acc_no)}"
                        mycur.execute(sql_Delete_ACC)
                        mydb.commit()
                        print("_________________________________________________________________________")
                        print("************* ACCOUNT HAS BEEN DELETED SUCCESSFULLY *******************")
                        print("_________________________________________________________________________")

                    elif ch1 == 7:
                        print("_____________________________________________________________________________")
                        print("*************Thanks For Choosing EDFX Bank Of India *****************")
                        print("____________________________________________________________________________")
                        exit()

            else:
                print('----------------------------------------------------------')
                print(" Login Failed, Please Try Again:")
                print('-----------------------------------------------------------')

        if ch==3:
            Admin_u_name=input("Enter Admin User Name Here: ")
            Admin_pwd=input("Enter Admin Password Here: ")
            sql_admin="select * from bank where User_Name ='{}' and Password ='{}'".format(Admin_u_name,Admin_pwd)
            mycur.execute(sql_admin)
            result=mycur.fetchall()
            if result:
                 while True:
                    print("---------------------")
                    print("WELCOME ADMIN")
                    print("---------------------")
                    print("\n")
                    print("Press 1 To View Account Holder Details")
                    print("Press 2 To View most Transactions made by User")
                    print("Press 3 To View Bank Total Fund")
                    print("Press 4 To Delete Your Account Permanently")
                    print("Press 5 To Log Out")

                    ch3 = int(input("Enter Your choice Here: "))
                    try:

                        if (ch3 >= 6):
                            raise TypeError("")
                    except TypeError:
                        print("oops!! that was an invalid input")
                    if ch3==1:
                            try:
                                acc_no=input("Enter the account number: ")
                                view_acc_holder_details=f"select * from bank where Account_no={int(acc_no)}"
                                mycur.execute(view_acc_holder_details)
                                re1=mycur.fetchall()
                                if re1:
                                    print("-------------------------------------")
                                    print("***** Account Holders Details ******")
                                    print("-------------------------------------")
                                    for item in re1:
                                        print(f"Account Number: {item[0]}")
                                        name = f'{item[1]}' +''+f'{item[2]}'
                                        print(f"Account Holder's Name: {name}")
                                        print(f"User Name of the Account Holder's: {item[3]}")
                                        print(f"Password of the Account Holder's: {item[4]}")
                                        print(f"date Of Birth of the Account Holder's: {item[5]}")
                                        print(f"Address of the Account Holder: {item[6]}")
                                        print(f"mobile  number of the account Holder's:{item[7]}" )
                                        print(f"Aadhar Number of the Account Holdr's: {item[8]}")
                                        print(f"Balance of the Account Holder's: {item[9]}")

                            except:
                                print("error")
                    elif ch3==2:
                        try:
                           most_transact=("""
                                SELECT t1.user_name, COUNT(t1.user_name) as num_transactions
                                FROM bank t1
                                JOIN transaction t2 ON t1.user_name=t2.user_name
                                GROUP BY t1.user_name
                                ORDER BY num_transactions DESC
                                LIMIT 1;
                                """)
                           mycur.execute(most_transact)
                           re2=mycur.fetchone()
                           print("\n")
                           print("Most Transactions made By User is :", re2[0])
                           print("Most Transactions is: ", re2[1])
                           print("\n")
                        except:
                            print("error")

                    elif ch3==3:
                        try:
                            total_fund="select SUM(Balance) from bank "
                            mycur.execute(total_fund)
                            re3=mycur.fetchone()
                            print("\n")
                            print("-------------------------------------")
                            print("Total fund of the Bank:",re3[0])
                            print("-------------------------------------")
                            print("\n")
                        except:
                            print("Error")

                    elif ch3==4:
                        try:
                            acc_no=input("Enter the account number to be deleted: ")
                            sql_Delete_Acc = f"DELETE FROM bank WHERE account_no={int(acc_no)}"
                            mycur.execute(sql_Delete_Acc)
                            mydb.commit()
                            print("_________________________________________________________________________")
                            print("************* ACCOUNT HAS BEEN DELETED SUCCESSFULLY *******************")
                            print("_________________________________________________________________________")
                        except:
                            print("Error")


                    elif ch3 == 5:
                        print("_____________________________________________________________________________")
                        print("*************Thanks For Choosing EDFX Bank Of India *****************")
                        print("____________________________________________________________________________")
                        exit()

            else:
                print("Admin login failed")
    except Exception:
        print("\n")
        print("-------------------------------------------------------------------------------")
        print("****************** OOPS!! The Username is Not available ************************")
        print("--------------------------------------------------------------------------------")





