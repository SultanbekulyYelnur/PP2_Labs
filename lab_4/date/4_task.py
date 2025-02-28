from datetime import datetime, timedelta

date1 = datetime(2025, 2, 22, 14, 30, 0)
date2 = datetime(2025, 2, 21, 12, 15, 0)

difference = abs((date1 - date2).total_seconds())

print(difference)