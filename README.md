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

Inorder to understand which fields give a greater indication as to whether or not a loan will be approved. It is important to look at the data from multiple angles. Of the 13 fields available I looked at all fields except Loan_ID and Loan Status to build my model. While not all these fields give a strong indication as to whether or not a loan woould be approved it does help see how certain fields can sway the overall model.

## Exploration.

![Applicant Income](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_applicant_income.png)
![Credit History](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_credit_history.png)
![Education](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_education.png)
![Married](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_married.png)
![Property Area](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_property_area.png)
![Self Employed](https://github.com/mikeyPower/loan-predication/blob/master/explore/output_self_employed.png)

## Understanding The Classification Report

**Precision**
Precision is the ability of a classiifer not to label an instance positive that is actually negative. For each class it is defined as as the ratio of true positives to the sum of true and false positives. Said another way, “for all instances classified positive, what percent was correct?”

Precision – Accuracy of positive predictions.
Precision = TP/(TP + FP)

**Recall**
Recall is the ability of a classifier to find all positive instances. For each class it is defined as the ratio of true positives to the sum of true positives and false negatives. Said another way, “for all instances that were actually positive, what percent was classified correctly?”

Recall: Fraction of positives that were correctly identified.
Recall = TP/(TP+FN)

**f1 score**
The F1 score is a weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0. Generally speaking, F1 scores are lower than accuracy measures as they embed precision and recall into their computation. As a rule of thumb, the weighted average of F1 should be used to compare classifier models, not global accuracy.

F1 Score = 2*(Recall * Precision) / (Recall + Precision)

**Support**
Support is the number of actual occurrences of the class in the specified dataset. Imbalanced support in the training data may indicate structural weaknesses in the reported scores of the classifier and could indicate the need for stratified sampling or rebalancing. Support doesn’t change between models but instead diagnoses the evaluation process.

## Understanding the Confusion Matrix

## References
https://www.scikit-yb.org/en/latest/api/classifier/classification_report.html
