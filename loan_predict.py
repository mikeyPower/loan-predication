import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import seaborn as sn
import sys
import matplotlib.pyplot as plt

train = sys.argv[1]
test = sys.argv[2]

# Training Data

df = pd.read_csv(train)
sn.countplot('Married', hue='Loan_Status', data=df)
plt.show()
plt.savefig("output.png")

df.fillna(-1,inplace=True)
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
print(accuracy_score(y_test,y_pred))

# Predicting the outcome of our test data using above model

y_pred2 = logistic_regression.predict(testing_data)
print(y_pred2)
