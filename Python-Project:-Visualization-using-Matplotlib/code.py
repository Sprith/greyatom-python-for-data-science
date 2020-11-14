# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data["Loan_Status"].value_counts()

#Add figure
fig_bar = plt.figure(figsize=[15,10])

#Add axes
ax_bar = fig_bar.add_axes([0,0,0.5,0.5])

#Set labels
ax_bar.set_xlabel("Loan Status")
ax_bar.set_ylabel("Count")

#Set Title
ax_bar.set_title("Distribution of loan statues")

#Plot the graph
bar = loan_status.plot(kind = "bar")

#Show the graph
plt.show()


# --------------
#Code starts here

# Group the loans
property_and_loan = data.groupby(["Property_Area","Loan_Status"]).size()
property_and_loan

#Unstacking the rows into columns and vice versa (helps in making a 2x2 matrix)

property_and_loan = property_and_loan.unstack()
property_and_loan

#Add the figure
fig_stack = plt.figure(figsize=(10,7))

#Add the axes
ax_stack = fig_stack.add_axes([0,0,1,1])

#Name the axes
ax_stack.set_xlabel("Property Area")
ax_stack.set_ylabel("Loan Status")

#Add title
ax_stack.set_title("Property Area vs. Loan Status")

#Plot the graph
bar_stack = property_and_loan.plot(kind='bar', stacked=False, ax = ax_stack)

#Rotate the x-axis label
ax_stack.set_xticklabels(ax_stack.get_xticklabels(), rotation=45, ha='right')




# --------------
#Code starts here

education_and_loan = data.groupby(["Education","Loan_Status"]).size().unstack()

#Create the figure canvas
fig_stack = plt.figure(figsize=(10,7))

#Add axes
ax_stack = fig_stack.add_axes([0,0,0.8,0.8])

#Label the axes
ax_stack.set_xlabel("Education Status")
ax_stack.set_ylabel("Loan Status")

#Add the title
ax_stack.set_title("Education vs. Loan")

#Plot the graph
bar_stack = education_and_loan.plot(kind = "bar", stacked=True, ax = ax_stack)

#Rotate the x-axis label
ax_stack.set_xticklabels(ax_stack.get_xticklabels(), rotation=45, ha='right')

#Show the graph
plt.show()


# --------------
#Code starts here

#Create two dataframes:- graduate and non-graduates
graduate = data[data["Education"] == 'Graduate']
graduate.head()

not_graduate = data[data['Education'] == 'Not Graduate']
not_graduate.head()


#Create the figure canvas
fig_scatter = plt.figure(figsize=(10,7))

#Add axes
ax_scatter = fig_scatter.add_axes([0,0,0.8,0.8])

#Label the axes
# ax_scatter.set_xlabel("Education Status")
# ax_scatter.set_ylabel("Loan Status")

# #Add the title
# ax_scatter.set_title("Education vs. Loan")

#Plot the graph
graduate_scatter = graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate_scatter = not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#Show the graph
plt.show()








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_2.set(title='Coapplicant Income')


#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_3.set(title='Total Income')


#Code ends here


