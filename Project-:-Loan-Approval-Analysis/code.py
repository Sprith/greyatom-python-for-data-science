# --------------
import pandas as pd

bank = pd.read_csv(path)


categorical_var = bank.select_dtypes('object')
print(categorical_var)

numerical_var = bank.select_dtypes('number')
print(numerical_var)


# --------------
# code starts here

banks = bank.drop("Loan_ID",axis=1)
banks.head()

print(banks.isnull().sum())

bank_mode = banks.mode()
print(bank_mode)

banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

import numpy as np

avg_loan_amount = banks.pivot_table(values='LoanAmount',index=['Gender','Married',
'Self_Employed'],aggfunc = np.mean)

avg_loan_amount


# code ends here



# --------------
# code starts here

loan1 = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se = loan1['Self_Employed'].count()

loan2 = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = loan2['Self_Employed'].count()

loan_status = 614

percentage_se = (loan_approved_se)/loan_status
percentage_se = percentage_se*100

percentage_nse = (loan_approved_nse)/loan_status
percentage_nse = percentage_nse*100

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)



big_loan_term = loan_term[loan_term >= 25]
big_loan_term = big_loan_term.count()

# code ends here


# --------------
# code starts here


loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()

# code ends here


