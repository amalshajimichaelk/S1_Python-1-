from datetime import datetime
current_time=datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d , %H:%M:%S")
print(format_1)
format_2=current_time.strftime("")
print(format_2)