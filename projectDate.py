# print("Choose year (1900-2100) : ")
# print("Choose Monthly (January , Februay , March , April ,May , June ,July,August, September , October, November , December)")
# print("Day (1-31)")

def date_function_monthly():
    while True :
        date_monthly = input("First Monthly : ")
        
        if date_monthly in {"January", "March", "May",  "July", "August", "October", "December"}:
            while True:
                print("Day (1-31)")
                date_day = input("First day : ")
                if 1<= int(date_day) <=31 :
                    print(date_monthly +" " + date_day)
                    break
                else :
                    print("Try Again ")
                    continue 
            break

        elif date_monthly ==  "February":
            while True:
                print("Day (1-28)")
                date_day = input("First day : ")
                if 1<= int(date_day) <=28 :
                    print(date_monthly +" " + date_day)
                    break
                else :
                    print("Try Again ")
                    continue
            break
                
        elif date_monthly in  {"April" , "June" , "September" ,  "November"}:
            while True:
                print("Day (1-30)")
                date_day = input("First day : ")
                if 1<= int(date_day) <=30 : 
                    print(date_monthly +" " + date_day)              
                    break
                else :
                    print("Try Again ")
                    continue
            break
        
        else :
            print("Try Again")
            continue

def date_function():
    print("Choose year (1900-2100)  ")
    while True:
         date_year = input("First Year : ")
         if 1900 <= int(date_year) <= 2100 :
             print("Choose Monthly (January , Februay , March , April ,May , June ,July,August, September , October, November , December)")
             date_function_monthly()
             print(date_year)
             break
         else:
             print("Try again")
             continue 
         
         
date_function()
