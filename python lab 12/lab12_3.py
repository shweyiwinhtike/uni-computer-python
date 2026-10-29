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

# Test Output:
"""
Basic Test:
Get name: Mr. V HalfDevil
Get date: 08/03/2019
Get date: 08/03/2562
Get address: 123 BlueRose St. White Garden Red Grave City England 123456

Check Person:
Name: Mr. V HalfDevil
Birthdate: 08/03/2019
Address: 123 BlueRose St. White Garden Red Grave City England 123456

Check Employee:
Employee Info:
Name: Ms. Nico Goldstein
Birthdate: 14/02/2010
Address: 123 RedRose St. Black Garden Sword Saint City England 112233
Employed by: Devil May Cry Inc.
Start date: 20/04/2019

Employee Info:
Name: Mr. Nero VergilSon
Birthdate: 10/01/2008
Address: 123 RedRose St. Black Garden Sword Saint City England 112233
Employed by: Devil May Cry Inc.
Start date: 20/04/2019
Wage: 420

Not Employ:
Employee Info:
Name: Mr. V HalfDevil
Birthdate: 08/03/2019
Address: 123 BlueRose St. White Garden Red Grave City England 123456
Employed by: None
Start date: 08/03/2019
Salary: 0

PermEmployee:
Employee Info:
Name: Mr. Dante SpardaSon
Birthdate: 23/08/1901
Address: 123 BlueRose St. White Garden Red Grave City England 123456
Employed by: Devil May Cry Inc.
Start date: 23/08/2001
Salary: 666

Should be None:
None
None
None

Should be full info:
Department: Devil May Cry Inc.
Manager:
Employee Info:
Name: Mr. Dante SpardaSon
Birthdate: 23/08/1901
Address: 123 BlueRose St. White Garden Red Grave City England 123456
Employed by: Devil May Cry Inc.
Start date: 23/08/2001
Salary: 666
None
Employee:
Employee Info:
Name: Ms. Nico Goldstein
Birthdate: 14/02/2010
Address: 123 RedRose St. Black Garden Sword Saint City England 112233
Employed by: Devil May Cry Inc.
Start date: 20/04/2019
Employee Info:
Name: Mr. Nero VergilSon
Birthdate: 10/01/2008
Address: 123 RedRose St. Black Garden Sword Saint City England 112233
Employed by: Devil May Cry Inc.
Start date: 20/04/2019
Wage: 420
Employee Info:
Name: Mr. Dante SpardaSon
Birthdate: 23/08/1901
Address: 123 BlueRose St. White Garden Red Grave City England 123456
Employed by: Devil May Cry Inc.
Start date: 23/08/2001
Salary: 666
"""

















class Name:
    def __init__(self, t, f, l) -> None:
        self.setName(t, f, l)

    def setName(self, t, f, l):
        self._title = t
        self._firstName = f
        self._lastName = l

    def getFullName(self):
        return self._title + self._firstName + self._lastName
    
class Date():
    def __init__(self, d, m, y) -> None:
        self.setDate(d, m , y)

    def setDate(self, d, m, y):
        self._day = d
        self._month = m
        self._year = y

    def getDate(self):
        return f"{self._day}/{self._month}/{self._year}"
    
    def getDateBC(self):
        return f"{self._day}/{self._month}/{self._year + 543}"
    
class Address:
    def __init__(self) -> None:
        pass

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self._houseNo = houseNo
        self._street = street
        self._district = district
        self._city = city
        self._country = country
        self._postcode = postcode

    def getAddress(self):
        return f"{self._houseNo}, {self._street}, {self._district}, {self._city}, {self._country}, {self._postcode}"
    
