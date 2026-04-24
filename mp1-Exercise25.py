# Exercise 25
t_seconds = int(input("Enter number of seconds: "))

sec_in_day = 24 * 60 * 60
sec_in_hr = 60 * 60
sec_in_min = 60

days = t_seconds // sec_in_day
remaining_sec = t_seconds % sec_in_day

hours = remaining_sec // sec_in_hr
remaining_sec %= sec_in_hr

minutes = remaining_sec // sec_in_min
seconds = remaining_sec % sec_in_min

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")