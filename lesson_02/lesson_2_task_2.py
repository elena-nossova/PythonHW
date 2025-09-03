def is_year_leap(year):
   if year % 4 == 0:
    print("год:" + str(year) + " True")
   else:
    print("год:" + str(year) + " False")

is_year_leap(2024)
is_year_leap(2023)
is_year_leap(2004)
is_year_leap(2013)