def format_name(first_name, last_name):
    f_name = list(first_name.lower())
    l_name = list(last_name.lower())
    f_name[0] = f_name[0].upper()
    l_name[0] = l_name[0].upper()
    return "".join(f_name)+" "+"".join(l_name)

# print(format_name("bardia","dehbasti"))
#_________________________________________________________________
# CHallenge 10.1
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  month_index = month - 1
  if is_leap(year) and month ==2:
    month_days[1] = 29
  return month_days[month_index]
#🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
#_________________________________________________________________


