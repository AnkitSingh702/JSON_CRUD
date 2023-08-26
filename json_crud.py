import json

UserDict = {}
def crud():
    print(' 1 create \n 2 read \n 3 update \n 4 delete ')
    option= int(input('choose an option:- '))
    if option==1:
        def Create():
            userName = input("Enter Your Name :- ")
            password = input("Enter Your Password :-")
            mobile=int(input("enter your mobile number..."))
            info={"user_name":userName,"password":password}
            UserDict[mobile] = info
            with open('data.json','w') as userData:
                json.dump(UserDict,userData,indent=4)
                print('Your Account Created successfully...')
        Create()
        crud()
    elif option==2:
        def read():
            print(' 1)all data\n 2)only one')
            op= int(input('choose an option to read:- '))
            if op==1:
                with open('data.json','r') as userData:
                    allData = json.load(userData)
                    print(allData)
            elif op==2:
                mobile= input('enter your mobile no. :- ')
                with open('data.json','r') as userData:
                    allData = json.load(userData)
                    if mobile in allData:
                        print(allData[mobile])
                    else:
                        print('not exist.........')
            else:
                print('invalid option...')
        read()
        crud()
    elif option==3:
        def update():
            mobile= input('enter mobile :- ')
            with open('data.json','r') as updating:
                data= json.load(updating)
                if mobile in data:
                    print(' 1 name\n 2 password\n 3 mobile')
                    opt= int(input('choose an option to update :- '))
                    if opt == 1:
                        new_name= input('enter new_name:= ')
                        data[mobile]['user_name'] = new_name
                        with open('data.json','w') as f:
                            json.dump(data,f,indent=4)
                            print('name updated successfully...')
                    elif opt == 2:
                        new_password= input("enter new password:= ")
                        data[mobile]['password'] = new_password
                        with open('data.json','w') as f:
                            json.dump(data,f,indent=4)
                            print("password updated successfully..")
                    elif opt == 3:
                        old_mob = input("enter old mobile number:= ")
                        if len(old_mob)==10:
                            print(data)
                            if old_mob in data:
                                new_mob= input('enter new mobile:= ')
                                if len(new_mob)==10:
                                    val= data.pop(old_mob)
                                    data[new_mob] = val 
                                    with open('data.json','w') as m:
                                        json.dump(data,m,indent=4)
                                        print("mobile updated successfully..")
                                else:
                                    print("please write a 10 digit number..")
                            else:
                                print("old mobile number does not match..")
                        else:
                            print("please write a 10 digit number..")
                else:
                    print('wrong mobile number..')
        update()
        crud()
    elif option == 4:
        def delete():
            old_mob = input("enter your old mobile := ")
            with open('data.json','r') as matchng:
                data= json.load(matchng) 
                if old_mob in data :
                    print("do you really want to delete your data..?\n yes \n no")
                    user= input("choose an option to move forward..")
                    if user == 'yes' :
                        del data[old_mob]
                        with open('data.json','w') as deleting:
                            json.dump(data,deleting,indent=4)
                            print("your data has been deleted..!!")
                    else:
                        print("Your data is safe ..!!")
                        crud()  
        delete()
        crud()   
crud()