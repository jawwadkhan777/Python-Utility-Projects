# print tables from 2 to the input range 
tables_range = int(input("Enter how much tables do you want to print:"))
print("your tables from 2 to",tables_range,'are:')
for x in range(2,tables_range+1):
    print("------- Table of", x,"-------")
    for y in range(1,11):
        table=x*y
        print("\t",x,'*',y,'=' ,table)


