import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import sys

input_file = sys.argv[1]


df = pd.read_csv(input_file)

df.fillna(-1,inplace=True)
df.Loan_Status.replace(('Y', 'N'), (1, 0), inplace=True)
df.Gender.replace(("Male","Female"),(1,0),inplace=True)
df.Married.replace(("Yes","No"),(1,0),inplace=True)
df.Education.replace(("Graduate","Not Graduate"),(1,0),inplace=True)
df.Self_Employed.replace(("Yes","No"),(1,0),inplace=True)
df.Property_Area.replace(("Urban","Rural","Semiurban"),(0,1,2),inplace=True)
df.Dependents.replace(("3+"),(3),inplace=True)
print(df)

print(df.Gender.unique())
print(df.Married.unique())
print(df.Dependents.unique())
print(df.Education.unique())
print(df.Self_Employed.unique())
print(df.Property_Area.unique())




X = df[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount',
'Loan_Amount_Term','Credit_History','Property_Area']]
y =df['Loan_Status']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

print(X_train)
print(y_train)

logistic_regression=LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)


confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)


print("Accuracy: ",metrics.accuracy_score(y_test, y_pred))
