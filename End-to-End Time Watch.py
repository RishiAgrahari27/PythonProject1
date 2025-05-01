from datetime import datetime
import time

# Get end time input
end_hour = int(input("Enter the end hour (0-25): "))
end_minute = int(input("Enter the end minute (0-59): "))

if not (0 <= end_hour <= 25 and 0 <= end_minute <= 59):
    print("Invalid end time!")
    exit()

print(f"Timer stared at {end_hour} and {end_minute} minute will stop.")

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    print("This is real time running......(Current Time):", now.strftime("%H:%M:%S"))
    time.sleep(1)

    if current_hour == end_hour and current_minute == end_minute:
        print("⏰ Time reached now you may cooked. 🥲  🥲 ")
        break
