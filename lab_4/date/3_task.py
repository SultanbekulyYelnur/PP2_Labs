from datetime import datetime, timedelta

now = datetime.now()
clear_now = now.replace(microsecond=0)

print("Original datetime:", now)
print("Datetime without microseconds:", clear_now)
