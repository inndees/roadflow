from dateutil import parser
from datetime import datetime
from dateutil.relativedelta import relativedelta

def days_diff_calc(date1, date2):
    # Calculate the difference in days between two dates
    # diff = abs((date2 - date1).days)
    diff = relativedelta(date2, date1)
    return diff

def end_date_calc(date_start, relative_delta):

    
    # Calculate the end date by adding the relative delta
    date2 = date_start + relative_delta

    return date2

# Print parsed dates
# date_today="2026-07-01"
# date_end="2026-07-16"
# difference=days_diff_calc(parser.parse(date_today),parser.parse(date_end))
# print("difference time:", difference)
# print("End date:", end_date_calc(parser.parse(date_today), difference))
