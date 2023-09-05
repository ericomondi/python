# Taking basic salary and benefits as inputs from the user
#  to calculate the gross salary 

basic_salary = int(input("Enter basic salary: "))
benefits = int(input("Enter benefits: "))

#  a function to calculate the gross salary

def findgross_salary(bs,b):
  gross_salary = basic_salary + benefits
  return gross_salary

# a variable to store the gross salary

gross_salary = findgross_salary(basic_salary, benefits)

# a function taking the gross salary to find the nhif contribution
    
def find_nhif(gross):
    if (gross_salary == 5999):
       nhif = 150
    elif (gross_salary >= 6000 and gross_salary <= 7999):
      nhif = 300
    elif (gross_salary >= 8000 and gross_salary <= 11999):
      nhif = 400 
    elif (gross_salary >= 12000 and gross_salary <= 14999):
      nhif = 500
    elif (gross_salary >= 15000 and gross_salary <= 19999):
      nhif = 600
    elif (gross_salary >= 20000 and gross_salary <= 24999):
      nhif = 750
    elif (gross_salary >= 25000 and gross_salary <= 29999):
      nhif = 850
    elif (gross_salary >= 30000 and gross_salary <= 34999):
      nhif = 900
    elif (gross_salary >= 35000 and gross_salary <= 39999):
      nhif = 950
    elif (gross_salary >= 40000 and gross_salary <= 44999):
      nhif = 1000
    elif (gross_salary >= 50000 and gross_salary <= 59999):
       nhif = 1200
    elif (gross_salary >= 60000 and gross_salary <= 69999):
        nhif = 1300
    elif (gross_salary >= 70000 and gross_salary <= 79999):
      nhif = 1400
    elif (gross_salary >= 80000 and gross_salary <= 89999):
      nhif = 1500
    elif (gross_salary >= 90000 and gross_salary <= 99999):
       nhif = 1600
    else :
      nhif = 1700
    return nhif
# a variable to store nhif

nhif = find_nhif(gross_salary)

# a function that takes the gross salary and pre-defined
# rate to find the nssf contribution

def find_nssf(gross, nssf_rate = 0.06):
  if (gross_salary <= 18000):
    nssf = gross_salary * nssf_rate
  else:
    nssf = 18000 * nssf_rate
  
  return nssf

#  a variable to store nssf contribution 

nssf = find_nssf(gross_salary)

# a function that takes the gross salary and pre defined rate
# to calculate the nhdf constribution

def find_nhdf(gross, nhdf_rate = 0.015):
  if (gross_salary <= 83334):
    nhdf = gross * nhdf_rate
  else:
    nhdf = 2500
  
  return nhdf

#  a variable to store nhdf constribution

nhdf = find_nhdf(gross_salary)

#  a function that calculates nhdf and nssf total

def findnssf_nhdftotal (nssf,nhdf):
  total = nssf + nhdf
  return total

# a variable to store nhdf and nssf total

nssf_nhdf_total = findnssf_nhdftotal(nssf,nhdf)

#  a function that takes the gross salary and 
#  nssf-nhdf total to calculate the taxable income

def find_taxable_income(gross,total):
    taxable_income = gross_salary - nssf_nhdf_total
    return taxable_income

#  a variable that stores taxable income

taxable_income = find_taxable_income(gross_salary, nssf_nhdf_total)

#  a function that takes the taxable income to find the payee

def find_payee(taxableIncome):
  personal_relief = 2400
  netpayee = 0
  if (taxable_income <= 24000):
    grosspayee = 24000 * 0.1
    netpayee = grosspayee - personal_relief
  elif (taxable_income <= 32333):
    grosspayee = (taxable_income - 24000) * 0.25 + 2400
    netpayee = grosspayee - personal_relief
  elif (taxable_income <= 500000):
    grosspayee = (taxable_income - 32333) * 0.3 + 4483.25
    netpayee = grosspayee - personal_relief
  elif (taxable_income <= 800000):
    grosspayee = (taxable_income - 500000) * 0.325 + 144783.35 + 2400
    netpayee = grosspayee - personal_relief
  else:
    grosspayee = (taxable_income - 800000) * 0.35 + 242283.35 + 2400
    netpayee = grosspayee - personal_relief
  
  return netpayee
# a variable to store the net payee

net_payee = find_payee(taxable_income)

# a function to calculate the net salary with this formula:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

def findnet_salary(gross,nhif,total, payee):
  net_salary = gross_salary - (nhif + nssf_nhdf_total + net_payee)
  return net_salary

#  a variable to store the net salary

net_salary = findnet_salary(gross_salary, nhif, nssf_nhdf_total,net_payee)

