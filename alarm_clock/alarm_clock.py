import sys

current_time = input("Podaj bieżący czas w formacie (HH:MM): ").replace(";", ":")
alarm_time = input("Podaj godzinę alarmu w formacie (HH:MM): ").replace(";", ":")

current_hours, current_minutes = current_time.split(":")
alarm_hours, alarm_minutes = alarm_time.split(":")

if (
    len(current_hours) != 2 or
    len(current_minutes) != 2 or
    len(alarm_hours) != 2 or
    len(alarm_minutes) != 2
):
    print("Podano nieprawidłowy format czasu (HH:MM)")
    sys.exit()

current_hours = int(current_hours)
current_minutes = int(current_minutes)
alarm_hours = int(alarm_hours)
alarm_minutes = int(alarm_minutes)

if (current_hours < 0 or current_hours > 23
        or alarm_hours < 0 or alarm_hours > 23):
    print("Podano nieprawidłowe godziny")
    sys.exit()

if (current_minutes < 0 or current_minutes > 59
        or alarm_minutes < 0 or alarm_minutes > 59):
    print("Podano nieprawidłowe minuty")
    sys.exit()

current_total = current_hours * 60 + current_minutes
alarm_total = alarm_hours * 60 + alarm_minutes
minutes_in_day = 24 * 60

minutes = None

if alarm_total >= current_total:
    minutes = alarm_total - current_total
else:
    minutes = (minutes_in_day - current_total) + alarm_total

print(f"Do alarmu pozostało: {minutes} minut.")