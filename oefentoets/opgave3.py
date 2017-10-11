class Employee:

    def __init__(self, name, role, department, salary_m):
        self.name = name
        self.role = role
        self.department = department
        self.salary_m = salary_m

    def __repr__(self):
        if self.salary_m > 1000:
            self.salary_m = float(self.salary_m /1000)

        return str({"name": self.name, "role": self.role, "department": self.department, "salary": str(self.salary_m)+"k"})



class Manager(Employee):

    def __init__(self, name, role, department, salary_m, bonus):
        super(Manager, self).__init__(name, role, department, salary_m)
        self.name = name
        self.role = role
        self.department = department
        self.salary_m = salary_m
        self.bonus = salary_m * (bonus / 100)
    # your code
    def __repr__(self):

        self.salary_m = float(self.salary_m /1000)
        self.bonus = float(self.bonus / 1000)

        return str({"name" : self.name, "role": self.role, "department": self.department, "salary": str(self.salary_m)+"k", "bonus": str(self.bonus)+"k"})


company = []
company.append(Manager('Murray', 'manager', 'finance', 5400, 10))
company.append(Manager('Bush', 'manager', 'R&D', 5400, 10))
company.append(Employee('Jasons', 'researcher', 'R&D', 2300))
company.append(Employee('Schneier', 'researcher', 'R&D', 4500))
company.append(Employee('Johnson', 'controller', 'finance', 2300))


for emp in company:
    print(emp)
