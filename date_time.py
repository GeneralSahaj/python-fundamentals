# Date and Time

import datetime

# =========================
# DATE OBJECTS
# =========================

date = datetime.date(2027, 4, 3)
today = datetime.date.today()

# =========================
# TIME OBJECTS
# =========================

time = datetime.time(4, 20, 0)

# =========================
# CURRENT DATE & TIME
# =========================

now = datetime.datetime.now()

# Store a formatted version separately
formatted_now = now.strftime("%H:%M:%S %d-%m-%Y")

# =========================
# DATE COMPARISON
# =========================

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

# =========================
# OUTPUT
# =========================

print("\n========== DATE & TIME REPORT ==========\n")

print(f"Specific Date     : {date}")
print(f"Today's Date      : {today}")

print()

print(f"Specific Time     : {time}")

print()

print(f"Current Datetime  : {now}")
print(f"Formatted Datetime: {formatted_now}")

print()

print("========== DATE COMPARISON ==========")

print(f"Target Datetime   : {target_datetime}")
print(f"Current Datetime  : {current_datetime}")

print()

if target_datetime < current_datetime:
    print("Status            : Target date has passed")
else:
    print("Status            : Target date has NOT passed")

print("\n=======================================\n")