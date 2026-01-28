import re

def change_date_format(dates):
    # Split the input string into individual dates
    date_list = [date.strip() for date in dates.split(',')]
    valid_dates = []
    
    for date in date_list:
        # Check if the date matches the format 'dd/mm/yyyy'
        if re.match(r'(\d{2})/(\d{2})/(\d{4})', date):
            day, month, year = map(int, date.split('/'))
            
            # Check for valid month
            if 1 <= month <= 12:
                # Determine the number of days in the month
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    days_in_month = 31
                elif month in [4, 6, 9, 11]:
                    days_in_month = 30
                elif month == 2:
                    # Check for leap year
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        days_in_month = 29
                    else:
                        days_in_month = 28
                else:
                    days_in_month = 0
                
                # Check if the day is valid for the given month
                if 1 <= day <= days_in_month:
                    # Convert the date format from 'dd/mm/yyyy' to 'mm/dd/yyyy'
                    valid_dates.append(f'{month:02d}/{day:02d}/{year}')
                else:
                    return f'{date} is not a valid date!'
            else:
                return f'{date} is not a valid date!'
        else:
            return f'{date} is not a valid date!'
    
    # Join the valid dates with commas and return the result
    return ', '.join(valid_dates)

# Test cases