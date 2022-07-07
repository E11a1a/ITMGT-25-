'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

grossPay = int (input("Input gross pay (in centavos) "))
taxRate = float (input("Input income tax rate "))
expenseCount = int (input ("Input expenses (in centavos) "))
def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    grossPayCentavoToPeso = gross_pay * 0.01
    expensesCentavoToPeso = expenses * 0.01

    taxed_income = (grossPayCentavoToPeso * (1-tax_rate))
    revenue = taxed_income -  expensesCentavoToPeso

    print(revenue)

savings(grossPay, taxRate, expenseCount)

totalMaterial = int (input("Input total material "))
materialUnits = str (input("Input material units (i.e. kg, L) "))
numJobs = int (input("Input number of jobs ")) 
jobConsumption = int (input("Input job consumption "))
def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    5 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    available_material = num_jobs * job_consumption
    remaining_material = str (total_material - available_material)
    print(str(remaining_material + material_units))
material_waste(totalMaterial, materialUnits, numJobs, jobConsumption)

principal = int(input("Input your Principal "))
rate = float(input("input your Rate (in decimals) "))
periods = int(input("input your Number of Periods "))
def interest(principal, rate, periods):
    '''Interest.
    5 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    centavoPrincipal = principal * 0.01
    
    first = centavoPrincipal * (rate * periods)
    second = int(first + centavoPrincipal)
    
    print(second)
    
interest(principal, rate, periods)    

ft = int (input("Input your height (ft) "))
inch = int (input("Input your height (inches) "))
weight = float(input ("Input your weight (lbs) "))
height = [ ft, inch ]
def body_mass_index(weight, height):
    '''Body Mass Index.
    5 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    lbtokg = weight/2.2
    fttom = height[0] *0.3048
    intom = height[1] *0.0254
    totalm = fttom + intom 
    BMI = lbtokg/(totalm ** 2)
    print (BMI)
    
body_mass_index(weight, height)  