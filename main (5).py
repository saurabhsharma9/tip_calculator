print("Welcome to the tip calculator")
bill = float(input("what is you total bill? $"))
#type total_bill
tip = int(input("what percentage of tip you would like to give? 10,12 or 15? "))
people = int(input("how many people split the bill?"))

tip_as_percent = tip/100
totaltip = bill*tip_as_percent
totalbill = bill+totaltip
billperperson = totalbill/people
finalamount = round(billperperson ,2)
finalamount = "{:.2f}".format(billperperson)
print(f"Each person should pay: ${finalamount}")
