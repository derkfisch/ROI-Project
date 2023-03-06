#Create a run function to calculate the rental's return on investment.

def run():
    
    #set each step (helper function) in class Return_roi() to the run function
    roi = Return_roi()
    roi.find_income()
    roi.find_expense()
    roi.find_cash_flow()
    roi.find_cash_on_cash()

    #set up while loop like in address book exercise to perform last steps
    #which will allow user to edit, view, or quit run function
    while True:
        close_out = input("Would you like to edit, view, or quit?")
              
        if close_out == 'edit':
            roi.edit()
        elif close_out == 'view':
            roi.view()
        elif close_out == 'quit':
            break

#create a class that with an __init__ method that the run function can refer to.
class Return_roi():

    #create an __init__ function that the helper functinos can refer to
    #set the starting point of each paramter to 0 to add to from inputs
    def __init__(self, m_income=0, m_expenses=0, m_cashflow=0, a_cashflow=0, investments=0, cash_on_cash=0):
        
        self.m_income = m_income
        self.m_expenses = m_expenses
        self.m_cashflow = m_cashflow
        self.a_cashflow = a_cashflow
        self.investments = investments
        self.cash_on_cash = cash_on_cash

    #All income must be inputted to calculate a total
    def find_income(self):

        #find all incomes
        rental_income_input = input("\nWhat is your monthly rental income? ")
        laundry_input = input('\nWhat is your monthly laundry income? ')
        storage_input = input('\nWhat is your monthly storage income? ')
        miscellaneous_input = input('\nWhat is your monthly miscellaneous income? ')

        #set their input values to integers
        rental_income = int(rental_income_input)
        laundry = int(laundry_input)
        storage = int(storage_input)
        miscellaneous = int(miscellaneous_input)

        #find the sum of these integers    
        self.m_income = sum([rental_income, laundry, storage, miscellaneous])
        print(f"\nYour total monthly income is ${self.m_income}")

    #All expenses must be inputted to calculate a total
    def find_expense(self):
        
        #find all expenses
        tax_input = input('\nWhat is your monthly tax expense? ')
        insurance_input = input('\nWhat is your monthly insurance expense? ')
        electricity_input = input('\nWhat is your monthly electricity expense? ')
        water_input = input('\nWhat is your monthly water expense? ')
        sewer_input = input('\nWhat is your monthly sewer expense? ')
        garbage_input = input('\nWhat is your monthly garbage expense? ')
        gas_input = input('\nWhat is your monthly gas expense? ')
        hoa_input = input('\nWhat is your Home Owners Association fee? ')
        vacancy_input = input('\nWhat is your monthly vacancy exepense? ')
        repairs_input = input('\nWhat is your monthly repairs expense? ')
        capital_expenditures_input = input('\nWhat is your monthly capital expenditures expense? ')
        property_management_input = input('\nWhat is your monthly property management expense? ')
        mortgage_input = input('\nWhat is your monthly mortgage expense?  ')

        #set all of the input values to integers
        tax = int(tax_input)
        insurance = int(insurance_input)
        electricity = int(electricity_input)
        water = int(water_input)
        sewer = int(sewer_input)
        garbage = int(garbage_input)
        gas = int(gas_input)
        hoa = int(hoa_input)
        vacancy = int(vacancy_input)
        repairs = int(repairs_input)
        capital_expenditures = int(capital_expenditures_input)
        property_management = int(property_management_input)
        mortgage = int(mortgage_input)

        #find the sum of all the monthly expenses    
        self.m_expenses = sum([tax, insurance, electricity, water, sewer, garbage, gas, hoa, vacancy, repairs, capital_expenditures, property_management, mortgage])
        print(f"Your total monthly expenses are ${self.m_expenses}")

    #Find the cash flow for monthly and annually
    #Need an equation from income and expenses
    def find_cash_flow(self):
        """calculate and print total monthly/annual cash flow from income and expenses."""
        
        #monthly cashflow is determined by subtracting your expenses from your income
        self.m_cashflow = self.m_income - self.m_expenses
        #annual cashflow would just be monthly cashflow * 12
        self.a_cashflow = self.m_cashflow * 12
        print(f"Your total monthly cashflow is ${self.m_cashflow} and your total annual cashflow is ${self.a_cashflow}")

    #find all the investment and use that number to find the 'cash on cash' roi
    def find_cash_on_cash(self):
     
        #find how much each investment cost      
        down_payment_input = input("\nWhat is your down payment? ")
        closing_input = input("\nWhat is your closing cost ?")
        rehab_input = input("\nWhat is your rehab budget? ")
        miscellaneous_investments_input = input("\nWhat is your miscellaneous investments? ")

        #set each input to an integer to add up
        down_payment = int(down_payment_input)
        closing = int(closing_input)
        rehab = int(rehab_input)
        miscellaneous_investments = int(miscellaneous_investments_input)

        #calculate total investment to help find cash on cash roi
        self.investments = sum([down_payment, closing, rehab, miscellaneous_investments])
        #cash on cash roi is annual cashflow dividede by total investment
        self.cash_on_cash = self.a_cashflow / self.investments
         
    #Create a helper function that will allow the user to view income, expenses, cashflows,
    #investments and cash on cash roi
    def view(self):
              
        #print a statement telling the user the total of each variable in the ROI equation    
        print("\nTotal monthly income $" + str(self.m_income) + ',')
        print("\nTotal monthly expenses $" + str(self.m_expenses) + ',')
        print('\nTotal monthly cashflow $' + str(self.m_cashflow) + ',')
        print('\nTotal annual cashflow $' + str(self.a_cashflow) + ',')
        print('\nTotal investment $' + str(self.investments) + ',')
        print('\nTotal cash on cash ROI' + str(self.cash_on_cash) + '%')

    #Create a helper function that will allow the user to edit all variables
    def edit(self):
        #find out which part the user wants to edit
        editor = input("\nwhich category would you like to edit? 'income', 'expenses', or 'investments'").lower()

        #if the user selects income, run the find_income function then set editted input back into the main function
        #set another helper function 'calculate' to define the editted input   
        if editor == 'income':
            self.find_income()
            self.calculate()
            self.view()
        #if the user selects expenses, run the find_expense function then set editted input back into the main function
        elif editor == 'expenses':
            self.find_expense()
            self.calculate()
            self.view()
        #if the user selects investments, run the find_cash_on_cash function then set editted input back into the main function
        elif editor == 'investments':
            self.find_cash_on_cash()
            self.calculate()
            self.view()

    #define the editted input
    def calculate(self):

        #same equations as before, just redefined for the new editted input
        self.m_cashflow = self.m_income - self.m_expenses
        self.a_cashflow = self.m_cashflow * 12
        self.cash_on_cash = self.a_cashflow / self.investments

run()