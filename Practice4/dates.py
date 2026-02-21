from datetime import datetime, timedelta




# Subtract five days from current date

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("Current date:", today)
print("Five days ago:", five_days_ago)




# Print yesterday, today, tomorrow

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:    ", today.date())
print("Tomorrow: ", tomorrow.date())




# Drop microseconds from datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("Original:", now)
print("Without microseconds:", no_microseconds)


# Calculate difference between two dates in seconds

date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 21, 14, 30, 0)

delta = date2 - date1
seconds = delta.total_seconds()

print("Date1:", date1)
print("Date2:", date2)
print("Difference in seconds:", seconds)