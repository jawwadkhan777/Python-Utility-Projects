# Program to generate all possible coordinates in 3-dimensions 
x = int(input("Enter x-axis range: "))
y = int(input("Enter y-axis range: "))
z = int(input("Enter z-axis range: "))
#n = int(input())
listx = [i for i in range (x+1)]
print ("x-axis possible value i.e. i-values: ",listx)
listy = [j for j in range (y+1)]
print ("y-axis possible value i.e. j-values: ",listy)
listz = [k for k in range (z+1)]
print ("z-axis possible value i.e. k-values: ",listz)
#final_list = [[i,j,k] for i in listx for j in listy for k in listz if i+j+k!=n]-->condition
final_list = [[i,j,k] for i in listx for j in listy for k in listz]
print("Possible coordinates in 3D are: ",final_list)