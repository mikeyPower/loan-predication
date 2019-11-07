import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import seaborn as sn
import sys
import matplotlib.pyplot as plt

train = sys.argv[1]
test = sys.argv[2]

# Some Investigation

df = pd.read_csv(train)
sn.countplot('Married', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output_married.png")
plt.clf()
sn.countplot('Education', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output_education.png")
plt.clf()
sn.countplot('Property_Area', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output_property_area.png")
plt.clf()
sn.countplot('Self_Employed', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output_self_employed.png")
plt.clf()
sn.countplot('Credit_History', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output_credit_history.png")
plt.clf()
sn.distplot(df['ApplicantIncome'],label='ApplicantIncome')
#sn.distplot(df['CoapplicantIncome'],label='CoapplicantIncome')
plt.savefig("output_applicant_income.png")
plt.clf()

print(df.groupby("ApplicantIncome").mean())
# Replace all empty spaces

df.fillna(-1,inplace=True)

# Need to convert options to numbers

df.Loan_Status.replace(('Y', 'N'), (1, 0), inplace=True)
df.Gender.replace(("Male","Female"),(1,0),inplace=True)
df.Married.replace(("Yes","No"),(1,0),inplace=True)
df.Education.replace(("Graduate","Not Graduate"),(1,0),inplace=True)
df.Self_Employed.replace(("Yes","No"),(1,0),inplace=True)
df.Property_Area.replace(("Urban","Rural","Semiurban"),(0,1,2),inplace=True)
df.Dependents.replace(("3+"),(3),inplace=True)


# Test Data

df2 = pd.read_csv(test)

df2.fillna(-1,inplace=True)
df2.Gender.replace(("Male","Female"),(1,0),inplace=True)
df2.Married.replace(("Yes","No"),(1,0),inplace=True)
df2.Education.replace(("Graduate","Not Graduate"),(1,0),inplace=True)
df2.Self_Employed.replace(("Yes","No"),(1,0),inplace=True)
df2.Property_Area.replace(("Urban","Rural","Semiurban"),(0,1,2),inplace=True)
df2.Dependents.replace(("3+"),(3),inplace=True)

# Get the columns we need for our trainning data

X = df[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount',
'Loan_Amount_Term','Credit_History','Property_Area']]
y =df['Loan_Status']

# Get the columns we need for our test data

testing_data = df2[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount',
'Loan_Amount_Term','Credit_History','Property_Area']]

# Building our model

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

logistic_regression=LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))

# ( TP + TN ) / Total

print(accuracy_score(y_test,y_pred))

# ( FP + FN ) / Total

print(1-accuracy_score(y_test,y_pred))

# visualize the prediction model

sn.heatmap(pd.DataFrame(confusion_matrix(y_test, y_pred)))
plt.show()
plt.savefig("heatmap.png")


# Predicting the outcome of our test data using above model

y_pred2 = logistic_regression.predict(testing_data)
print(y_pred2)
print("Number of loans approved: ",np.sum(y_pred2))
print("Number of loans not approved: ",len(y_pred2)-np.sum(y_pred2))