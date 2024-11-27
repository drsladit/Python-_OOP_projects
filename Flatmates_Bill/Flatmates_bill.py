
import os
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import webbrowser


class Bill:
    """
        Class creates bill object which contains data like amount and days.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
        Class creates Flatmate object which contains data like name and no of days.
        It als contain methods to generate bill for each flatmate
    """

    def __init__(self, name, no_of_days):
        self.name = name
        self.no_of_days = no_of_days
    

    def pays(self, bill, other_flatmate):
        """
            Function which calculates each flatmate amount to be paid.
        """
        weight = self.no_of_days / (self.no_of_days+other_flatmate.no_of_days)
        return bill.amount*weight


class PDFreport:
    """
        Create PDF file object which should have details of flatmate such as thier name, 
        thier bill amount and period of the bill

    """

    def __init__(self, filename):
        self.filename = filename


    def generatePDF(self, bill, flatmate1, flatmate2):
        '''
         Function which generate PDF file with flatmetes bill details.
        '''
        # Initialising FPDF 
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add title to the PDF file
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1) # w=0 and align='C' make difference

        # Insert billing month_year details
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=60, h=40, txt='Period:', border=0)
        pdf.cell(w=80, h=40, txt=bill.period, border=0, ln=1)


        # Insert name and bill of flatmate 1
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=60, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=80, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert name and bill of flatmates 2
        pdf.cell(w=60, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=80, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0)

        file_path = 'F:\Learning\Python_OOP_projects\Flatmates_Bill\PDF_files'
        location_filename = os.path.join(file_path, self.filename)
        pdf.output(os.path.join(location_filename))

        return location_filename


    def add_passwordPDF(self, pdfFile_location, password):
        '''
            Function which adds password to pdf file generated
        '''

        reader = PdfReader(pdfFile_location)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(pdfFile_location, "wb") as f:
            writer.write(f)

        webbrowser.open(pdfFile_location)