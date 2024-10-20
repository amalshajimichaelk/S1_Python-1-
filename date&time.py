'''
Author: Amal Shaji Michael
Date: 20-18-2024
Description: Familiarize time and date
             in various formats
             (Eg. “Thu Jul 11 10:26:23 IST 2024”).
             
2024-10-20 18:03:43.199986
2024-10-20 , 18:03:43

Sunday,October 20,2024
Sunday,October 20,2024 18:03:43 PM
Sun-Oct-20 18:03:43  2024

2024-10-20
18:03:43.199986
10
2024


'''


from datetime import datetime
current_time=datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d , %H:%M:%S")
print(format_1)
format_2=current_time.strftime("")
print(format_2)
format_3=current_time.strftime("%A,%B %d,%Y")
print(format_3)
format_4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format_4)
format_5=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
print(format_5)
format_6=current_time.strftime("%Z")
print(format_6)
current_date=current_time.date()
print(current_date)
format_7=current_time.time()
print(format_7)
format_8=current_time.month
print(format_8)
format_9=current_time.year
print(format_9)
