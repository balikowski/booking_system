import json 
from datetime import date, timedelta, datetime

FILE_NAME = "dates.json"
YEAR = 2026

first_day = date(YEAR, 1, 1)
last_day = date(YEAR, 12, 31)

current_day = first_day
idx = 0
dates = []

while current_day <= last_day:
    start = 8.0
    end = 16.0

    if current_day.weekday() <= 4: # skip weekends
        name = f"{start} - {start+1.0}"
        day = {}
        day["date"] = current_day.isoformat()
        slots = []
        while start <= end-1.0:
            slot = {"id": idx, "start": start, "end": start+1.0, "booked_by": ''}
            slots.append(slot)
            start += 1.0 
            idx += 1
        day["slots"] = slots 
        dates.append(day)
        

    current_day += timedelta(days=1)

with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(dates, file, indent=4, ensure_ascii=False)