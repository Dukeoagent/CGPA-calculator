name = input("Please enter your name: ")

#List (array) to store all SGPA
SGPA = []

#Input for no of sems done
completedSem = int(input ("Enter the number of semesters completed so far: "))

#Adding all SGPA to the list
for i in range(completedSem):
    val = float(input("Enter your SGPA for sem " + str(i+1) +": "))
    SGPA.append(val)

#Calculating current CGPA
CGPA = sum(SGPA)/len(SGPA)
CGPA = round(CGPA, 2)
print(f"Your current CGPA after {completedSem} semesters is: {CGPA}")

#Calculation of next semsters CGPA
temp = float(input(f"What is the minimum SGPA you believe you could get this semester: "))

#SGPA cannot exceed 10.0
while (temp<=10):
    result = (sum(SGPA) + temp) / (len(SGPA) + 1)
    #CGPA cannot exceed 10.0
    if(result <= 10):
        print(f"To get {round(result,2)} CGPA, I will need to score {round(temp,2)} SGPA")
        temp = temp + 0.1

print(f"Thank You for using my calculator {name}")        