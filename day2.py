#Write down your expenses for each day of the week (Sunday to Saturday).
Sunday_expn= 1500
monday_expn= 1000
tuesday_expn= 2000
wednesday_expn= 1750
thursday_expn=1800
friday_expn= 2000
saturday_expn=2500

#Find the total of all your expenses for the week.
total_expn = (Sunday_expn + monday_expn + tuesday_expn + wednesday_expn + thursday_expn + friday_expn + saturday_expn)
# Calculate the average daily expenses.
average_expn = (total_expn/7)
# print the both value
print(f"total expenses is: {total_expn}")
print(f"average daily expenses is: {average_expn}")
