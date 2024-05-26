# Machine-Learning
## Structure
The only deployable folder is: ML_API and is self contained. The rest lives on the repo and the repo only.

# This project Is structed in 4 main components:
   1. Datasets
       - The datasets required to train models
       - This folder is in the .gitignore

   2. Deployed Models
       - Model development is done here.  
       - When these models are deployed and compressed(PKL etc), they download to 
            'Machine Learning Projects/ML_API/Models/' folder where the ML_API serves them.
   3. ML_API
       - This is the flask API in charge of serving deployed models and data to consumers

# Secrets
Secrets config uses age
Dependencies: age

