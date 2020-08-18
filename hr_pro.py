import datetime

class Employee:
    #Employee class here
    def __init__(self, name, age, salary, employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year
    
    def get_working_years(self):
        today = datetime.datetime.now()
        return today.year - self.employment_year
    
    def __str__(self):
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}')


class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    
    def get_bonus(self):
        #print (bonus_percentage * salary)
        return self.bonus_percentage * self.salary
    
    def __str__(self):
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}, Bonus: {self.get_bonus()}')
    

        
def main():
    # main code here

    def main_input():
        name = input("Name: ")
        age = input("Age: ")
        salary = float(input("Salary: "))
        employment_year = int(input("Employment year: "))
        return [name, age, salary, employment_year]
    
    employee = []
    manager = []
    while True:

        print ("Welcome to HR Pro 2020\nOptions:")
        print ("\t 1. Show Employees")
        print ("\t 2. Show Managers")
        print ("\t 3. Add Employees")
        print ("\t 4. Add Managers")
        print ("\t 5. Exit")

        option = input("What would you like to do?")

        if option == "5":
            break

        elif option == "1":
            for i in employee:
                i.__str__()
        
        elif option == "2":
            for i in manager:
                i.__str__()

        elif option == "3":
            info = []
            info = main_input()
            employee.append(Employee(info[0], info[1], info[2], info[3]))
            print ("Employee added succesfully")

        elif option == "4":
            info = main_input()
            bonus = float(input("Bonus Percentage: "))
            manager.append(Manager(info[0], info[1], info[2], info[3], bonus))
            print ("Manager added succesfully")
        
        




if __name__ == '__main__':
	main()
