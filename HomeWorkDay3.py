############## Assignment 2##################
# Task 02: Create two list named as Actual Price and Tax with five different products.
# Then calculate each products sales price.
# You could show the results as a single list. Remember, you have to use loop.
ActualPrice_list = [25, 50, 75, 100, 125]
Tax_list = [14.5, 10.5, 8.5, 5.5, 10]
product_list=['apple','orange','grapes','banana','mango']
final_list=[]

for i in range(0, len(ActualPrice_list)):
    final_list.append(ActualPrice_list[i] + Tax_list[i])
    # final_list=str(final_list)
print(final_list)
############ Assignment 3##################
# Task 03: Write a function to find branch name from branch list. You must call this this function from a different python file.
def BranchList(bname):
    Branch_List=['Bogra','Bhairab','Barisal','Haziganj','Chittagong','Cumilla','Coxsbazar','Dinajpur','Rangpur']
    if bname in Branch_List:
        print(bname + ' is available in branch list')
    else:
        print('Sorry '+bname+' is not available in branch list')

