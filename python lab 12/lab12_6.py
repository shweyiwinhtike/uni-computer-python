import abc

# Add your Transportation classes here
    
    
# main program
wa1 = Walk("KMITL", "Lawson at KMITL", 0.6)
ta1 = Taxi("Lawson at KMITL", "Ladkrabang Station", 5)
tr1 = Train("Ladkrabang Station", "Payathai Station", 40, 6)
ta2 = Taxi("Payathai Station", "The British Council", 3)

transport = [wa1, ta1, tr1, ta2]
total = 0
for tran in transport:
    fc = tran.find_cost()
    print("Cost:", fc)
    total += fc
    
print("Total:", total)

# Test Output:
"""
Cost: 0.0
Cost: 200.0
Cost: 30.0
Cost: 120.0
Total: 350.0
"""