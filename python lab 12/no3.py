class Name:
    def __init__(self, t, f, l):
        self.setName(t, f, l)

    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return f"{self.title}. {self.firstName} {self.lastName}"


class Date:
    def __init__(self, d, m, y):
        self.setDate(d, m, y)

    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

    def getDateBC(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year + 543:04d}"


class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.setAddress(houseNo, street, district, city, country, postcode)

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return (
            f"{self.houseNo} {self.street} {self.district} "
            f"{self.city} {self.country} {self.postcode}"
        )


class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def printInfo(self):
        print(f"Name: {self.name.getFullName()}")
        print(f"Birthdate: {self.birthdate.getDate()}")
        print(f"Address: {self.address.getAddress()}")


class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department=None):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = None

        if isinstance(department, Department):
            department.addEmployee(self)

    def printInfo(self):
        print("Employee Info:")
        super().printInfo()

        if self.department is None:
            print("Employed by: None")
        else:
            print(f"Employed by: {self.department.description}")

        print(f"Start date: {self.startDate.getDate()}")


class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, wage, department=None):
        super().__init__(name, birthdate, address, startDate, department)
        self.wage = wage

    def printInfo(self):
        super().printInfo()
        print(f"Wage: {self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, salary, department=None):
        super().__init__(name, birthdate, address, startDate, department)
        self.salary = salary

    def __str__(self):
        return self.name.getFullName()

    def printInfo(self):
        super().printInfo()
        print(f"Salary: {self.salary}")


class Department:
    def __init__(self, description, manager=None):
        self.description = description
        self.manager = None
        self.employeeList = []

        if manager is not None:
            self.setManager(manager)

    def addEmployee(self, e):
        if e not in self.employeeList:
            self.employeeList.append(e)
            e.department = self

    def deleteEmployee(self, e):
        if e in self.employeeList:
            self.employeeList.remove(e)
            if e.department is self:
                e.department = None
            if self.manager is e:
                self.manager = None

    def setManager(self, e):
        if isinstance(e, PermEmployee) and e in self.employeeList:
            self.manager = e

    def printInfo(self):
        print(f"Department: {self.description}")
        print("Manager:")
        if self.manager is not None:
            self.manager.printInfo()
        else:
            print("None")

        print("Employee:")
        for e in self.employeeList:
            e.printInfo()


# Add your classes here


print("Basic Test:")
name1 = Name("Mr", "V", "HalfDevil")
print("Get name:", name1.getFullName())
bdate1 = Date(8, 3, 2019)
print("Get date:", bdate1.getDate())
print("Get date:", bdate1.getDateBC())
address1 = Address("123","BlueRose St.","White Garden","Red Grave City","England","123456")
print("Get address:", address1.getAddress())

print()
print("Check Person:")
p1 = Person(name1, bdate1, address1)
p1.printInfo()

dep = Department("Devil May Cry Inc.")

print()
print("Check Employee:")
name2 = Name("Ms", "Nico", "Goldstein")
bdate21 = Date(14, 2, 2010)
bdate22 = Date(20, 4, 2019)
address2 = Address("123","RedRose St.","Black Garden","Sword Saint City","England","112233")
e1 = Employee(name2, bdate21, address2, bdate22, dep)
e1.printInfo()

print()
name3 = Name("Mr", "Nero", "VergilSon")
bdate31 = Date(10, 1, 2008)
e2 = TempEmployee(name3,bdate31,address2,bdate22,420,dep)
e2.printInfo()

print()
print("Not Employ:")
e3 = PermEmployee(name1,bdate1,address1,bdate1,0)
e3.printInfo()

print()
print("PermEmployee:")
name4 = Name("Mr", "Dante", "SpardaSon")
bdate41 = Date(23, 8, 1901)
bdate42 = Date(23, 8, 2001)
e4 = PermEmployee(name4,bdate41,address1,bdate42,666,dep)
e4.printInfo()

print()
print("Should be None:")
dep.setManager(e1)
print(dep.manager)
dep.setManager(e2)
print(dep.manager)
dep.setManager(e3)
print(dep.manager)

print()
print("Should be full info:")
dep.setManager(e4)
dep.printInfo()