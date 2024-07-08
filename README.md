# Machine-Learning

## Structure
The only deployable folder is: ML_API and is self contained. The rest lives on the repo and the repo only.

# This project's main folders of interest are:
 
   1. `/Models`
       - Model development is located here.  
       - When these models are finished, they are deployed `deployed_models` folder

   2. `/deployed_models`
       - Deployed models from `Models` folder. 

   3. `/ML_API`
       - This is the flask API in charge of serving deployed models from `deployed_models` and data to consumers.

   4. `/datasets`
       - The datasets required to train models
       - This folder is in the .gitignore
 

# Secrets
Secrets config uses age
Dependencies: age

