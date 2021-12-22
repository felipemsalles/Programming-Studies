# 1061
starting_day = int(input().split()[1])
moment = input().split(" : ")
#
initial_hour = int(moment[0])
initial_minute = int(moment[1])
initial_second = int(moment[2])
#
last_day = int(input().split()[1])

moment = input().split(" : ")
final_hour = int(moment[0])
final_minute = int(moment[1])
final_second = int(moment[2])
#
days_duration = last_day - starting_day
days_hours = final_hour - initial_hour
days_minutes = final_minute - initial_minute
days_seconds = final_second - initial_second
#
if days_hours < 0:
    days_hours += 24
    days_duration -= 1

if days_minutes < 0:
    days_minutes += 60
    days_hours -= 1

if days_seconds < 0:
    days_seconds += 60
    days_minutes -= 1

print("{} day(s)".format(days_duration))
print("{} hour(s)".format(days_hours))
print("{} minute(s)".format(days_minutes))
print("{} second(s)".format(days_seconds))