# THIS IS STUDENT INFO ENTRY SYSTEM:

import csv
def write_into(info_list):
     with open('StudentAdmin.csv','a',newline='') as csv_file:
          writer=csv.writer(csv_file)
          
          if (csv_file.tell()==0):
               writer.writerow(['S.NO.','NAME','AGE','CLASS','SECTION','EMAIL-ID','CONTACT_NO.'])
               
          writer.writerow(info_list)
########################################################
def remember_count():
     result=[]
     try:
          with open('StudentAdmin.csv') as csv_file:
               reader=csv.DictReader(csv_file)
               for row in reader:
                    result.append(row)
              
          return result[-1]['S.NO.']
     except:
          return 1
########################################################

condition=True


num=remember_count()

if num==1:
     counter=1
else:
     counter=int(num)+1



while(condition):
     

     student_info=input('ENTER THE STUDENT #{} INFORMATION IN FOLLOWING FORMAT:-\n(NAME AGE CLASS SECTION EMAIL-ID CONTACT_NO.)\n[SEPERATE ENTRIES WITH <SPACE> OR ","]:'
                        .format(counter))

     info=student_info.split(' 'or',')
     info.insert(0,counter)

     print('THE ENTERED INFORMATION IS:\nNAME={}\nAGE={}\nCLASS={}\nSECTION={}\nEMAIL-ID={}\nCONTACT_NO.={}'
           .format(info[1],info[2],info[3],info[4],info[5],info[6]))
     print('-------------------------------------------------------------------')

     check1=input('IS THE ENTER INFORMATION CORRECT?(YES/NO):\n').casefold()
     if check1=='yes':
          write_into(info)
          counter+=1
          print('-------------------------------------------------------------------')
          again=input("DO YOU WANT TO ENTER ANOTHER STUDENT'S INFORMATION?(YES/NO):\n").casefold()
          if(again == 'yes'):
               condition=True
          elif(again=='no'):
               condition=False

     elif check1=='no':
          print('PLEASE RE-ENTER CORRECT INFORMATION!!!')

     
########################################################         
