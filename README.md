# loan-predication

## Prerequisite
    ./install.sh requirements.txt
    
## Run
    python loan.py <test_data> <train_data>
    
## Demo
![image](https://user-images.githubusercontent.com/17595044/68384081-c0af1d00-014e-11ea-861e-358a7f8a2c96.png)


Training Data:

| Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area | Loan_Status |
| ------- | ------ | ------- | ---------- | --------- | ------------- | --------------- | ----------------- | ---------- | ---------------- | -------------- | ------------- | ----------- |
| LP001002 | Male   | No     | 0           | Graduate | No             | 5849           | 0                 |            | 360              | 1              | Urban          | Y           |


Test Data:

| Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area |
| ------- | ------ | ------- | ---------- | --------- | ------------- | --------------- | ----------------- | ---------- | ---------------- | -------------- | ------------- |
| LP001015 | Male   | No     | 0           | Graduate | No             | 5720           | 0                 | 110        | 360              | 1              | Urban         | 
