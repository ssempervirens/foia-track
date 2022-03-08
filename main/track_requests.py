# get today's requests and print/format them nicely
from datetime import date

def track_requests(cursor):
    # decrease days_to_followup by one each time script is run
    cursor.execute(
        "UPDATE requests SET days_to_followup = days_to_followup - 1 WHERE days_to_followup > 0"
    )
    pass

def get_today_requests(cursor):
    cursor.execute(
        "SELECT * FROM requests WHERE days_to_followup=0"
    )

# each time script is run, decrease days_to_followup by one? or calculate if days since date requested is divisible by followup interval?