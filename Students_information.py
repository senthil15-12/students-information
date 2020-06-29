import csv
def info(inf_list):
    with open ('Students_inf.csv' ,  'a+' , newline = '') as csv_file :
        w = csv.writer(csv_file)
       
        if csv_file.tell () == 0 :
            w.writerow (["Name","Age","Contact_Number","Mail_ID"])
        w.writerow (inf_list)
        
if(__name__=='__main__') :     
    check= True
    stud_num=1

while (check):
        Students_inf = input("Enter students informartion for student #{} in the order of (Name Age Contactnumber MailId): ".format(stud_num))
        print("Entered information: " + Students_inf)
        
        Stud_inf_list= Students_inf.split(",")
        print("Entered split information: " + str(Stud_inf_list))
        print("\nThe Entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nMail_ID: {}\n".format(Stud_inf_list[0],Stud_inf_list[1],Stud_inf_list[2],Stud_inf_list[3]))
        cho=input("Is the entered information correct (Y/N)\n: ")
        if cho=="Y":
            info(Stud_inf_list)
            con_check= input("Enter (Y/N) if you want to add another student information\n")
            if con_check=="Y":
                check=True
                stud_num=stud_num+1
                
            elif con_check=="N":
                check=False
                
            
        elif cho=="N":
            print("\n Please re-enter the values")
            
            
            output:
            Enter students informartion for student #1 in the order of (Name Age Contactnumber MailId): ajay,12,9442156512,aja12@gmail.com
Entered information: ajay,12,9442156512,aja12@gmail.com
Entered split information: ['ajay', '12', '9442156512', 'aja12@gmail.com']

The Entered information is -
Name: ajay
Age: 12
Contact_Number: 9442156512
Mail_ID: aja12@gmail.com

Is the entered information correct (Y/N)
: Y
Enter (Y/N) if you want to add another student information
Y
Enter students informartion for student #2 in the order of (Name Age Contactnumber MailId): Senthil,23,8750761234,sen33@gmail.com
Entered information: Senthil,23,8750761234,sen33@gmail.com
Entered split information: ['Senthil', '23', '8750761234', 'sen33@gmail.com']

The Entered information is -
Name: Senthil
Age: 23
Contact_Number: 8750761234
Mail_ID: sen33@gmail.com

Is the entered information correct (Y/N)
: N

 Please re-enter the values
Enter students informartion for student #2 in the order of (Name Age Contactnumber MailId): Senthil,19,9486725510,sen15@gmail.com
Entered information: Senthil,19,9486725510,sen15@gmail.com
Entered split information: ['Senthil', '19', '9486725510', 'sen15@gmail.com']

The Entered information is -
Name: Senthil
Age: 19
Contact_Number: 9486725510
Mail_ID: sen15@gmail.com

Is the entered information correct (Y/N)
: Y
Enter (Y/N) if you want to add another student information
N
In [ ]:


​
                
                
