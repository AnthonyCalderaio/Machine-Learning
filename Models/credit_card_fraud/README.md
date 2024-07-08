# Model

# Performance
At the evaluation stage of this model we checked for overfitting. Here were the results:

---- Evaluate if overfitted ---
<br />
`Training Score: 0.9991836555553117` <br />
`Testing Score: 0.9989466661985184`

As you can see: The training and test set perform very closely in numbers and not only that, they both perform very high. No signs of overfitting. It might be worth using cross-validation to validate the robustness of the model.


---- Cross validation (k=5) --- 
<br />
`0.99940749` <br/>
`0.99923193` <br/>
`0.99927582` <br/>
`0.99888082` <br/>
`0.99934166` <br/>
<br/>
Mean CV accuracy:  <br/>
`0.9992275450415852`

As we can see, the models performances are absurdly high. Lets take a look at the actual data: one of the columns in this dataset is the 'fake' column with a "1" for fake and "0" for real with 492 instances of the row indicating it is "fake" and the rest (56,000+) more instances of not-fake rows. This is a large class imbalance and could likely be affecting the absurdly high accuracy scores for this model. If we take a look at the accuracy report...

              precision    recall  f1-score   support

           0       1.00      1.00      1.00     56864
           1       0.74      0.60      0.66        98

    accuracy                            1.00     56962
    macro avg       0.87      0.80      0.83     56962
    weighted avg    1.00      1.00      1.00     56962

It becomes more clear. We can see the recall score for the "1" (Fake) class is so low while the inverse is so high. Furthermore, we can validate here the class counts are imbalanced.


## Class imbalance

To tackle the class imbalance issue, we will try a few things...


Attempt 2: we can try adding a class weight to the classifer but this ended up with a worse f1 scrore.  <br/>


`sample_weights = compute_sample_weight(class_weight='balanced', y=y_train)`<br/>
`model = GradientBoostingClassifier()`<br/>
`model.fit(X_train, y_train, sample_weight=sample_weights)`<br/>

               precision    recall  f1-score   support

            0       1.00      0.99      1.00     56864
            1       0.18      0.93      0.31        98

    accuracy                            0.99     56962
    macro avg       0.59      0.96      0.65     56962
    weighted avg    1.00      0.99      1.00     56962
-----------------------------------------------------------------<br/><br/>


Attempt 3: we will try the threshold optimization <br/> 


`model = GradientBoostingClassifier()` <br/>
`model.fit(X_train, y_train)` <br/>
`y_proba = model.predict_proba(X_test)[:, 1]` <br/>
`threshold = 0.24` <br/>
`y_pred = (y_proba >= threshold).astype(int)` <br/>


               precision    recall  f1-score   support

            0       1.00      1.00      1.00     56864
            1       0.75      0.69      0.72        98

    accuracy                            1.00     56962
    macro avg       0.87      0.85      0.86     56962
    weighted avg    1.00      1.00      1.00     56962

  as you can see, we have achieved an f1-score of 0.72 which is the highest we have achieved so far.

-----------------------------------------------------------------