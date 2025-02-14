from datetime import datetime

current_date = datetime.now().replace(microsecond=0)  # Убираем микросекунды
b = current_date.strftime("%Y-%m-%d %H:%M:%S")

print(b)
