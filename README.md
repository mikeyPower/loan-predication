# loan-predication

## Prerequisite
    ./install.sh requirements.txt
    
## Run
    python loan.py <test_data> <train_data>
    
## Demo
![image](https://user-images.githubusercontent.com/17595044/68384081-c0af1d00-014e-11ea-861e-358a7f8a2c96.png)

Understanding the Data:

There are a total of 13 fields in the training data and 12 in that of the test data. The only field missing from that of the testing data is that of Loan status which we are too predict.

    Loan ID: The ID given by the bank to the loan request.
    Gender: The gender of the primary applicant.
    Married: Binary variable indicating the marital status of the primary applicant.
    Dependents: Number of dependents of the primary applicant.
    Education: Binary variable indicating whether or not the primary applicant has graduated high school.
    Self_Employed: Binary variable indicating whether or not the individual is self-employed.
    Applicant Income: The income of the primary applicant.
    Co-Applicant Income: The income of the co-applicant.
    Loan Amount: The amount the applicant wants to borrow.
    Loan Amount Term: The term over which the applicant would repay the loan.
    Credit History: Binary variable representing whether the client had a good history or a bad history.
    Property Area: Categorical variable indicating whether the applicant was from an urban, semiurban, or a rural area.
    Loan Status: Variable indicating whether the loan was approved or denied. This will be our output (dependent) variable.

Training Data:

| Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area | Loan_Status |
| ------- | ------ | ------- | ---------- | --------- | ------------- | --------------- | ----------------- | ---------- | ---------------- | -------------- | ------------- | ----------- |
| LP001002 | Male   | No     | 0           | Graduate | No             | 5849           | 0                 |            | 360              | 1              | Urban          | Y           |


Test Data:

| Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area |
| ------- | ------ | ------- | ---------- | --------- | ------------- | --------------- | ----------------- | ---------- | ---------------- | -------------- | ------------- |
| LP001015 | Male   | No     | 0           | Graduate | No             | 5720           | 0                 | 110        | 360              | 1              | Urban         | 


Which Fields to pick?

Inorder to understand which fields give a greater indication as to whether or not a loan will be approved. It is important to look at the data from multiple angles. Of the 13 fields available I looked at all fields except Loan_ID and Loan Status to build my model. While not all these fields give a strong indication as to whether or not a loan woould be approve it does help see how certain fields can sway the model.
