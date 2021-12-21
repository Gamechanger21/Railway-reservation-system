import tkinter as tk
import pandas as pd
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='root',database='railway')
print('successfully connected')



class Main(object):
    def menu():
        print()
        print("**************************************************")
        print(   "WELCOME TO RAILWAY RESERVATION SYSTEM"    )

        print("1. Check PNR Status.")
        print(".Show Train Detail's")
        print("3.Show Passenger Detail's")
        print("4.Reservation of ticket")
        print("5.Cancellation of reservation")
    
    


    menu()

        
        
        #PNR is the abbreviation of "PASSENGER NAME RECORD" and
        #it is also called used as a booking number




    def showtrainsdetail():
         print('ALL TRAINS DETAIL')  
         df=pd.read_sql("select * from trainsdetail",conn)
         print(df)


    def showpassengers():
         print('ALL PASSENGERS DETAIL')  
         df=pd.read_sql("select*from passengers",conn)
         print(df)


    def disp_pnrno():
         print("PNR STATUS WINDOW")
         a=(input("ENTER TRAIN NO.  : "))
         qry="select pnameID,status from passengers where trainno=%s;"%(a,)
         df=pd.read_sql(qry,conn)
         print(df)

    def ticketreservation():
         print("WE HAVE THE FOLLOWING SEAT TYPES FOR YOU:-")
         print("TNAME IS 1 FOR GOA EXPRESS FROM NEW DELHI")
         print()
         print(" 1.FIRST CLASS AC RS 6000 PER PERSON")
         print("2.SECOND CLASS AC RS 5000 PER PERSON")
         print("3.THIRD CLASS AC RS 4000 PER PERSON")
         print("4.FOR SLEEPER RS 3000 PER PERSON")
         print()

         print("TNAME IS 2 FOR JAMMU EXPRESS FROM NEW DELHI")
         print()
         print(" 1.FIRST CLASS AC RS 10000 PER PERSON")
         print("2.SECOND CLASS AC RS 9000 PER PERSON")
         print("3.THIRD CLASS AC RS 8000 PER PERSON")
         print("4.FOR SLEEPER RS 7000 PER PERSON")
         print()

         tname=(input("ENTER YOUR CHOICE OF TRAIN NAME PLEASE->"))
         print(tname)
         x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE->"))
         n=int(input("HOW MANY TICKETS YOU NEED:"))
         
         if(x==1):
             print("YOU HAVE CHOSEN FIRST CLASS AC TICKET")
             s=6000*n
         elif(x==2):
             print("YOU HAVE CHOSEN SECOND CLASS AC TICKET")
             s=5000*n
         elif(x==3):
             print("YOU HAVE CHOSEN THIRD CLASS AC TICKET")
             s=4000*n 
         elif(x==4):
             print("YOU HAVE CHOSEN SLEEPER TICKET")
             s=3000*n 
         else:
             print("Invalid option")

         if(x==1):
             print("YOU HAVE CHOSEN FIRST CLASS AC TICKET")
             s=10000*n
         elif(x==2):
             print("YOU HAVE CHOSEN SECOND CLASS AC TICKET")
             s=9000*n
         elif(x==3):
             print("YOU HAVE CHOSEN THIRD CLASS AC TICKET")
             s=8000*n 
         elif(x==4):
             print("YOU HAVE CHOSEN SLEEPER TICKET")
             s=7000*n 
         else:
             print("Invalid option")     

             print("Please choose a train")
             print("your TOTAL TICKET PRICE is =",s,"\n")
    def      cancel():
             print("Before any changes in the status:")   
             df=pd.read_sql("select*from passengers",conn)
             print(df)
             mc=conn.cursor()
             mc.execute("update passengers set status='cancelled'where pnrno='G1001'")
             #conn.commit()
             df=pd.read_sql("select*from passengers",conn)
             print(df)
    opt=""
    opt=int(input("Enter your choice: "))
    if opt==1:
        disp_pnrno()
    elif opt==2:
        showtrainsdetail()
    elif opt==3:
        showpassengers()
    elif opt==4:
        ticketreservation
    elif opt==5:
        cancel()
    else:
        print('Invalid Option')

        def main():
          mainwin = Tk()
          app = Main(mainwin)
          mainwin("RAILWAY RESERVATION SYSTEM")
          mainwin.geometry('900x900')
          mainwin.mainloop()
