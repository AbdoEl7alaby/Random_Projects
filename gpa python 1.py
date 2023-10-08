'''
GPA calculator for AOU students
Author : Abdo El7alaby
'''
def course_calc (x,y):
    if x >= 90:
        print("Your grade in \"", y, "\" is : A")
    elif 82 <= x <= 89:
        print("Your grade in \"", y ,"\"is : B+")
    elif 74 <= x <= 81:
        print("Your grade in \"", y ,"\" is : B")
    elif 66 <= x <= 73:
        print("Your grade in \"", y ,"\" is : C+")
    elif 58 <= x <= 65:
        print("Your grade in \"", y, "\" is : C")
    elif 50 <= x <= 57:
        print("Your grade in \"", y ,"\" is : D")
    else :
        print("You failed \"", y,"\"" )

print("==============================================")
print("============= AOU GPA CALCULATOR =============")
print("==============================================")
n = int(input("Number of courses : "))
j = 0
i = 0
k = 0
l = 0
sub = list(range(1,n+1))
hours = list(range(1,n+1))
points = list(range(1,n+1))
name = list(range(1,n+1))

for j in range (n):
    print("------------------------------------------------------------------")
    name[j] = str(input("Name of the cousre : "))
    sub[j] = float(input("Total grades : "))
    hours[j] = int(input("Number of hours : "))
    j = j + 1

for k in range (n):
    if sub[k] >= 90:
        points[k] = 4
    elif 82 <= sub[k] <= 89:
        points[k] = 3.5
    elif 74 <= sub[k] <= 81:
        points[k] = 3
    elif 66 <= sub[k] <= 73:
        points[k] = 2.5
    elif 58 <= sub[k] <= 65:
        points[k] = 2
    elif 50 <= sub[k] <= 57:
        points[k] = 1.5
    else :
        points[k] = 0
        
t_points = 0
t_hours = 0

for i in range (n):
    t_points = t_points + (points[i]*hours[i])
    t_hours = t_hours + hours[i]
GPA = round(t_points / t_hours , 2 )
print("==============================================")
for l in range (n):
    course_calc (sub[l],name[l])
print("==============================================")
print("Your total hours :", t_hours )
print("Your GPA :",GPA)
print("==============================================")
enter = eval(input("Enter to END"))
if enter == "" :
    pass
else : pass
