from datetime import datetime

date_string = input()

formatted_date = datetime.strptime(date_string, "%m %d %Y")

print(formatted_date.strftime("%A").upper())
