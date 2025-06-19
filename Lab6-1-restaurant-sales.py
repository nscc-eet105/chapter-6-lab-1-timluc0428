#Tim Lucas
#Lab 6-1 
#2025 - 06 - 18

#create a tuple to hold the spelled-out days of the week.
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#create an empty list for daily sales amount
daily_sales = []

#use week tuple in a for loop to prompt for each day's sales. 
    #prompt user for sales amount for each day of week. and store in a list. 
for day in days:
    daily_sales.append(float(input(f"Enter the sales amount for {day}\t : ")))

#calculate total weekly sales
total_sales = sum(daily_sales)

#calculate average weekly sales
average_weekly_sales = total_sales / len(days)

#calculate minimum daily sales amount
lowest_sales = min(daily_sales)

#find the lowest day
lowest_day = days[daily_sales.index(lowest_sales)]

#calculate maximum daily sales amount
highest_sales = max(daily_sales)

#find highest day
highest_day = days[daily_sales.index(highest_sales)]

#display total weekly sales
print()
print(f"Total weekly sales\t: ${total_sales:.2f}")

#display average weekly sales
print(f"Average weekly sales\t: ${average_weekly_sales:.2f}")

#display the minimum daily sales amount, and what day it occurred
print()
print(f"The highest sales were ${highest_sales:.2f} on {highest_day}")

#display the maximum daily sales amount, and what day it occurred
print(f"The lowest sales were ${lowest_sales:.2f} on {lowest_day}")

