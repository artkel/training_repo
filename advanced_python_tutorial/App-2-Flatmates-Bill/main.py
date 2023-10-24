from flat import Bill, Flatmate
from reports import PdfReport

period = input("Enter the period (Month-YYYY): ")
amount = float(input("Enter the bill amount in USD: "))

flatmate1_name = input("What's the 1st flatmate's name? ")
flatmate1_days = int(input(f"How many days did {flatmate1_name} spend home in {period}? "))

flatmate2_name = input("What's the 2nd flatmate's name? ")
flatmate2_days = int(input(f"How many days did {flatmate2_name} spend home in {period}? "))


the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days)

print(f"{flatmate1.name} pays: {flatmate1.pays(bill=the_bill, flatmate2=flatmate2)} USD")
print(f"{flatmate2.name} pays: {flatmate2.pays(bill=the_bill, flatmate2=flatmate1)} USD")

pdf_report = PdfReport(filename=f"reports\Report_{period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
