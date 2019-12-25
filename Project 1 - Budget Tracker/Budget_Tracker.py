import sys

class Budget():
    def __init__(self):
        self.income = 0
        self.expense = 0
        self.expense_list = []
        self.expense_name = []
        self.income_list = []
        self.income_name = []
        self.prompt_income
        self.prompt_expense
        
    def income_prompt(self):
        add_income = input('Add Income? [y/n]: ')
        return add_income
        
    def income_sum(self):
        self.income = sum(self.income_list)
        
    def expense_prompt(self):
        add_expense = input('Add Expense? [y/n]:')
        
    def expense_sum(self):
        self.expense = sum(self.expense_list)
        
    def income_check(self):
        if not self.income_list:
            print ('Please enter one source of income.')
            self.prompt_income()
        else:
            return
        
    def expense_check(self):
        if not self.expense_list:
            print ('PLease enter one expense.')
            self.prompt_expense()
        else:
            return
        
    def prompt_income(self):
        x = False
        while not x:
            result = self.income_prompt()
            if result == 'y':
                income_input = int(input('Enter income (number'))
                self.income_list.append(income_input)
                income_name = input('Enter name for source of income')
                self.income_name.append(income_name)
            else:
                self.income_check()
                x = True
        name = [name for name in self.income_name]
        income = [income for income in self.income_list]
        incomedict = dict(zip(name, income))
        for i in incomedict:
            print(i + ': ', '$' + str(incomedict[i]))
        print('Total user income: ', '$' + str(self.income))
        self.prompt_expense
        
    def prompt_expense(self):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':
                expense_input = int(input('Enter expense (number)'))
                self.expense_list.append(expense_input)
                expense_name = input('Enter name for expense')
                self.expense_name.append(expense_name)
            else:
                self.expense_check
                x = True
        name = [name for name in self.expense_name]
        expense = [expense for expense in self.expense_list]
        expensedict = dict(zip(name, expense))
        for e in expensedict:
            print(e + ': ', '$' + str(self.expense[e]))
        print('Total user expense: ', '$' + str(self.expense))
        self.uservalue()
        
    def uservalue(self):
        valoutput = self.income - self.expense
        if valoutput < 0:
            print('You are in the negative, you have a deficit of ' + '$' + str(valoutput))
        if valoutput == 0:
            print('You have broken even, you are spending exactly as much as you make')
        if valoutput > 0:
            print('You are in the positive, you have a surplus of ' + '$' + str(valoutput))
        another = input('Would you like to run another analysis? [y/n]')
        if another == 'y':
            self.reset_program()
        if another == 'n':
            self.close_program()
            
    def reset_program(self):
        self.income = 0
        self.expense = 0
        del self.expense_list[0:]
        del self.expense_name[0:]
        del self.income_list[0:]
        del self.income_name[0:]
        self.prompt_income
    
    def close_program(self):
        print('Closing program...')
        sys.exit(0)
        
if __name__=='__main__':
Application()
                
            
    
    
