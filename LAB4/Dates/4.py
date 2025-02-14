from datetime import datetime,timedelta

current_date = datetime.now()

tomorrow = (current_date + timedelta(days=1)).timestamp()
yesterday = (current_date - timedelta(days=1)).timestamp()

print(f"Разница в секундах: {tomorrow - yesterday}")

