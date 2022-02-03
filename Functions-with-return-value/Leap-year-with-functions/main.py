def is_leap(year):
  is_leap_year="False"
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        is_leap_year="True"
        return is_leap_year
      else:
        return is_leap_year
    else:
      is_leap_year="True"
      return is_leap_year
  else:
    return is_leap_year

def days_in_month(f_year,f_month):
  result_year=""
  result_year=is_leap(f_year)

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if result_year:
    return (month_days[f_month -1]+ 1)
  else:
    return (month_days)
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












