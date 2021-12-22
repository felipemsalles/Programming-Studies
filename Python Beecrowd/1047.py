# 1047
initial_hour, initial_minute, final_hour, final_minute = input().split(" ")
initial_hour = int(initial_hour)
initial_minute = int(initial_minute)
final_hour = int(final_hour)
final_minute = int(final_minute)

total_hours = final_hour - initial_hour

if total_hours < 0:
    total_hours += 24
total_minutes = final_minute - initial_minute

if total_minutes < 0:
    total_minutes += 60
    total_hours -= 1
    if total_hours < 0:
        total_hours += 24

if total_minutes == 0 and total_hours == 0:
    print("GAME DURATION 24 HOUR(S) AND  0 MINUTE(S)")
else:
    print("GAME DURATIONS {} HOUR(S) AND {} MINUTE(S)".format(total_hours, total_minutes))