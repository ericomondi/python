class Payroll():
    basic_salary = 0
    benefits = 0
    

    def __init__(self, bs = int(input("Enter basic salary: ")),
                  b = int(input("Enter benefits: "))):
        self.basic_salary = bs
        self.benefits = b
        self.find_gross_salary()
        self.find_nhif()
        self.find_nssf()
        self.find_nhdf()
        self.find_nssf_nhdf_total()
        self.find_taxable_income()
        self.find_payee()
        self.find_netsalary()

    def find_gross_salary(self):
        self.gross_salary = self.basic_salary + self.benefits
        print(f'The gross salary is {self.gross_salary}')
    
    def find_nhif(self):

        if (self.gross_salary == 5999):
            self.nhif = 150
        elif (self.gross_salary >= 6000 and self.gross_salary <= 7999):
            self.nhif = 300
        elif ( self.gross_salary>= 8000 and self.gross_salary <= 11999):
            self.nhif = 400 
        elif (self.gross_salary >= 12000 and self.gross_salary<= 14999):
            self.nhif = 500
        elif (self.gross_salary >= 15000 and self.gross_salary <= 19999):
            self.nhif = 600
        elif (self.gross_salary >= 20000 and self.gross_salary <= 24999):
            self.nhif = 750
        elif (self.gross_salary >= 25000 and self.gross_salary <= 29999):
            self.nhif = 850
        elif (self.gross_salary >= 30000 and self.gross_salary <= 34999):
             self.nhif = 900
        elif (self.gross_salary >= 35000 and self.gross_salary <= 39999):
            self.nhif = 950
        elif (self.gross_salary >= 40000 and self.gross_salary <= 44999):
            self.nhif = 1000
        elif (self.gross_salary >= 50000 and self.ross_salary <= 59999):
            self.nhif = 1200
        elif (self.gross_salary >= 60000 and self.gross_salary <= 69999):
            self.nhif = 1300
        elif (self.gross_salary >= 70000 and self.gross_salary <= 79999):
            self.nhif = 1400
        elif (self.gross_salary >= 80000 and self.gross_salary <= 89999):
            self.nhif = 1500
        elif (self.gross_salary >= 90000 and self.gross_salary <= 99999):
            self.nhif = 1600
        else :
            self.nhif = 1700
        print(f'Your NHIF contribution is {self.nhif}')

    def find_nssf(self, rate = 0.06):
        if self.gross_salary <= 18000:
            self.nssf = self.gross_salary * rate
        else:
            self.nssf = 18000 * rate
        print(f'Your NSSF contribution is: {self.nssf}')

    def find_nhdf(self, rate = 0.015):
        if self.gross_salary <= 83334:
            self.nhdf = self.gross_salary * rate
        else:
            self.nhdf = 2500
        print(f'Your NHDF contribution is {self.nhdf}')

    def find_nssf_nhdf_total(self):
        self.nssf_nhdf_total = self.nssf +self.nhdf
        print(f'NSSF-NHDF total is {self.nssf_nhdf_total}')

    def find_taxable_income(self):
        self.taxable_income = self.gross_salary - self.nssf_nhdf_total
        print(f'The taxable income is {self.taxable_income}')

    def find_payee(self,personal_relief = 2400):
        self.netpayee = 0
        if (self.taxable_income <= 24000):
            grosspayee = 24000 * 0.1
            self.netpayee = grosspayee - personal_relief
        elif (self.taxable_income <= 32333):
            grosspayee = (self.taxable_income - 24000) * 0.25 + 2400
            self.netpayee = grosspayee - personal_relief
        elif (self.taxable_income <= 500000):
            grosspayee = (self.taxable_income - 32333) * 0.3 + 4483.25
            self.netpayee = grosspayee - personal_relief
        elif (self.taxable_income <= 800000):
            grosspayee = (self.taxable_income - 500000) * 0.325 + 144783.35 + 2400
            self.netpayee = grosspayee - personal_relief
        else:
            grosspayee = (self.taxable_income - 800000) * 0.35 + 242283.35 + 2400
            self.netpayee = grosspayee - personal_relief
        print(f'The net Payee is {self.netpayee}')

    def find_netsalary(self):
        # net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
        self.net_salary = self.gross_salary - (
            self.nhif + self.nhdf + self.nssf + 
            self.netpayee
        )
        print(f'The net salary is {self.net_salary}')


       
Payroll()