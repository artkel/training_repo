import webbrowser
from fpdf import FPDF
from flat import Bill, Flatmate


class PdfReport:
    """"
    Creates a pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files\house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=140, txt='Flatmate bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the 1st flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt='$' + str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # Insert name and due amount of the 2nd flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt='$' + str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        # Insert total bill amount
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=40, txt='Total', border=0)
        pdf.cell(w=150, h=40, txt='$' + str(bill.amount), border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


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
