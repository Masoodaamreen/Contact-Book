print("CONTACT BOOK")
print('''1.Add a new contact
2.Search for an exsisting contact
3.Delete an existing contact
4.Display all contacts ''')
operation=int(input("Enter the number of the operation you want to perform:"))
contacts={"Ammu": 9876543210,"Affu":9345678123,"Moin":9988776655,"Moez":9012345678,"Yasmeen":9367854321,"Tabassum":9234567890,"Basha":9900112233,"Bathul":9654321098 ,"Mohammed":9786543219}
def display_contacts():
    for name,number in contacts.items():
        print(f" {name}= {number}")

def add_contact():
 try:
    a=str(input("Enter a new name:"))
    new_name= a.capitalize()
    new_number=input("Enter the new number:")
    if new_name in contacts:
        print("Contact name already exists")
        add_contact()
    elif not new_number.isdigit():
        print("invalid input! the number should be an integer")
        add_contact()
    elif len(new_number)!=10:
        print("invalid input! the number should be 10 digits")
        add_contact()
    elif new_number in contacts:
        print("Contact number already exists")
        add_contact()
    elif new_name not in contacts and new_number not in contacts:
        contacts.setdefault(new_name,new_number)
        print("contact added!")
        display_contacts()
        want_to_add_again()
 except ValueError:
     print("invalid input")
     add_contact()
     
     
def want_to_add_again():
    want_to_add=str(input('''*Want to add a new contact? "yes" or "no": '''))
    if want_to_add=="yes" or want_to_add=="Yes" or want_to_add=="YES":
        add_contact()
    elif  want_to_add=="no" or want_to_add=="No" or want_to_add=="NO":
        print("your contacts") 
        display_contacts()
        want_perform_more_operations()
    else:
        print('''invalid! enter"yes"or "no"''')
        want_to_add_again()
        
        
        

def search_contact():
 try:
    search_type=int(input('''Search contact by 1.Name or 2.Number
    *Enter 1 or 2:'''))
    if search_type==1:
        x=str(input("*Enter the name of contact to search:"))
        search_name=x.capitalize()
        if search_name in contacts:
            print(f"{search_name}'s number is {contacts[search_name]}")
            want_to_search_again()
        else:
            print("The contact doesn't exists")
            want_to_search_again()
            
    elif search_type==2:
       try: 
         search_number=int(input("*Enter the number of contact to search:"))
       except ValueError:
          print("enter only integer")
          search_contact()
       if len(str(search_number))!=10:
           print("invalid Enter only 10 digits")
           search_contact()
       elif len(str(search_number))==10:
            for name, number in contacts.items():
                if number == search_number:
                    print(f"The number {search_number} belongs to {name}")
                    want_to_search_again()
                    break   
            else:
                 print("The contact doesn't exist.")
                 want_to_search_again()
    else:
        print("invalid! enter only 1 or 2")
        search_contact()
 except ValueError :
     print("invalid input! Enter valid number")
     search_contact()
            
            
            
            
def want_to_search_again():
    search_again=str(input("*want to search again? yes or no:"))
    if search_again=="yes" or search_again =="Yes" or search_again=="YES":
        search_contact()
    elif search_again=="no" or  search_again=="No" or search_again=="NO":
        want_perform_more_operations()
    else:
        print('''invalid! enter"yes"or "no"''')
        want_to_search_again()
        
        
def want_perform_more_operations():
    more_operaions=str(input("*want to perform more operation? enter yes or no:"))
    if more_operaions=="yes" or more_operaions=="Yes" or more_operaions=="YES":
     print('''1.Add a new contact
2.Search for an exsisting contact
3.Delete an existing contact
4.Display all contacts ''')
     operation_num=int(input("Enter the number of the opertion you want to perform:"))
     if operation_num==1:
       add_contact()
     elif operation_num==2:
       search_contact()
     elif operation_num==3:
      delete_contact()
     elif operation_num==4:
       display_all_conatcts()
     else:
       print("Invalid input! choose only between 1-4")
    elif more_operaions=="no" or more_operaions=="No" or more_operaions=="NO":
        print("Here is your final contact book")
        display_contacts()
    else:
        print("invalid input! enter only yes or no")
        want_perform_more_operations()

            
          
          
def delete_contact():
    delete=int(input('''*Want to delete by 1.Name or 2.Number
    choose 1 or 2:'''))
    if delete==1:
        i=str(input("Enter the contact name you want to delete:"))
        del_name=i.capitalize()
        if del_name in contacts:
            del contacts[del_name]
            print(" The updated contacts")
            display_contacts()
            want_to_delete_again()
        elif del_name not in contacts:
            print("contact doesnt exists")
            want_to_delete_again()
        else:
            print("invalid! input")
    elif delete==2:
        del_number=int(input("Enter the contact number you want to delete:"))
        for name,number in list(contacts.items()):
            if number==del_number:
                del contacts[name]
                print(f"successfully deleted {name}={number} contact ")
                print("Here is your updated contacts ")
                display_contacts()
                want_to_delete_again()
                break
        else:
            print("contact doesn't exists")
            want_to_delete_again()
            
    else:
        print("Invalid input enter 1 or 2")
        
        
def want_to_delete_again():
    want_to_del=str(input('''*Want to delete another contact? "yes" or "no": '''))
    if want_to_del=="yes" or want_to_del=="Yes" or want_to_del=="YES":
        delete_contact()
    elif  want_to_del=="no" or want_to_del=="No" or want_to_del=="NO":
        print("Your contacts") 
        display_contacts()
        want_perform_more_operations()
    else:
        print('''invalid! enter"yes"or "no"''')
        want_to_delete_again()
        


def display_all_conatcts():
    display_contacts()
    want_perform_more_operations()
         
        
        
if operation==1:
    add_contact()
elif operation==2:
    search_contact()
elif operation==3:
    delete_contact()
elif operation==4:
    display_all_conatcts()
else:
    print("Invalid inputQ choose only between 1-4")