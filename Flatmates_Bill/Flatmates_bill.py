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
    

    def bill_generation(self, bill, other_flatmate):
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
    

    def generatePDF(self, flatmate1, flatmate2, bill):
        pass


