![Credit card image gotten from usplash.com](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/nathana-reboucas-ND5HWK6Ivrg-unsplash.jpg)

# Machine-Learning-zoomcamp-Midterm-project

This repo contains project work I carried out as the midterm project in the [mlzoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp).  The course was organised by [Alexy Grigorev](https://github.com/alexeygrigorev).

## Table of contents

- [1. About the project](#topic1)
- [2. Project files and folder explained](#topic2)
- [3. Running this project](#topic3)



<h2 id="topic1"> 1. About the project</h2>

Credit card fraud can be defined as any fraud or theft that involves a credit card. Credit card fraud aims to purchase goods or steal money with someone else credit account. Advance in modern-day technology has created more room for credit card fraud. Since the invention of online purchases, perpetrators no longer need a physical card to make an unauthorized purchase. Additionally, electronic databases containing credit card data can get hacked or crash on their own, releasing customers' credit card information. These electronic database hacks put the security of many accounts at risk at once.

Common forms of credit card fraud include:

- Lost or stolen cards are used without their owner's permission.

- Credit cards are 'skimmed,' where the card is cloned or copied using a special swipe machine to create a duplicate.

- Card details, such as the card number, cardholder name, date of birth, and address, are stolen from online databases or through email scams. These stolen details are then sold and utilized for fraud on the internet or over the phone. This type of fraud is often referred to as 'card-not-present' fraud.

- Fraudulent applications are made in someone else's name for a new credit card, without the person's knowledge or consent.

The goal of this project is to build a fraud detection system using machine learning. This system will have the ability to classify an online credit card transaction as fraudulent or not fraudulent based on the transaction details. The machine learning model will learn from past credit card transaction data and use the patterns it learns from the data to identify if a new transaction is fraudulent or not. Furthermore, the model will be hosted as a web service that accepts credit card transaction details in a JSON data format and returns a prediction of whether the transaction is fraudulent or not. Deploying this model as a web service will be beneficial to financial institutions, banks, or online stores as they can easily feed transaction details to the machine learning system and the model will return its prediction. This can help dectecting in potential fraud in trade and therefore get the transaction flagged and declined. By identifying potential instances of fraud, companies can take steps to prevent fraudulent activity from occurring, which can save them a significant amount of money loss.

### Challenges in credit card fraud detection
- It's not always easy to agree on the ground truth for what "fraud" means.
- Most of the transactions are tagged as not fraudulent, therefore leading to a class imbalance of the dataset
- Fraud detection dataset contains sensitive pieces of information, therefore a lot of data representations a usually hidden

### Summary
- I picked a problem to solve with machine learning (credit card fraud detection)
- Used Kaggle dataset for (EDA and modeling)
- Decided to go with xgboost model because of the class imbalance of the dataset
- One feature I noticed from the model is that, the farther the transaction is from home, the more likely it is fraudulent
- Deployed the model as a web service using Flask, I containerize the app with docker and deployed the docker container to a cloud 
  provider (AWS elastic beanstalk)
- The deployed service takes transaction details as a JSON file and returns a prediction for the transaction as fraudulent or not.
  
  > *Note* I was not able to deploy the web service to a cloud service provider because of difficulties in creating an AWS account 
using my country's payment method. I am currently working on resolving this, I will update the change when I resolve this.
  
<h2 id="topic2"> 2. Project files and folder explained</h2>

### Data
 > This folder gives you access to the data used in this project
### Images 
 > This is a folder of images I used in this project
### Pipfile and Pipfile.lock
 > These are dependencies management files used to create a virtual environment for the machine learning project. This is to ensure the 
   reproducibility of the project.
### credit card fraud detection.ipynb
 > This is a Jupyter notebook that contains the codes I used for data preparation, EDA(Explanatory data analysis), model training/selection, and hyperparameter tuning. It also contains code for saving the final model. For this, I used pickle.
### Dockerfile
 > This is a docker image file, this file is used to create instances of a docker container. It defines what will happen in the docker container.
### Predict.py 
 > This is a Python script used to create a Flask app to run the prediction service. It's a web service.
### request.py
 >This script sends a request to the web service(predict.py) which accepts transaction details and returns the prediction of whether the transaction is fraudulent or not. I used one transaction detail to run this request.
### train.py
 > This is a Python script for training the model. This script contains code I used to train my final model
### xgb_model.bin.
 > This is the model used for the prediction, it is saved to disk.


<h2 id="topic3"> 3. Running this project</h2> 
To run this project, follow these steps. Navigate to your command line and enter these commands.

### Step 1: Clone the repo

`git clone https://github.com/cyberholics/mlzoomcamp-midterm-project.git`

### Step 2: Enter the project directory

`cd mlzoomcamp-midterm-project/`

### Step 3: Install dependencies

`pipenv install`

### Step 4: Train the model

- Open the train.py script with your preferred code editor, I recommend VScode
- Download the dataset with this [link](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/Data/data.md)
- Edit this code. Replace it with the  path of the downloaded dataset. i.e the location the data is saved on your PC
  
![code to edit](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-06%20at%2011.01.52.png) 

- Run the training script with this command `python train.py`
  You should get an output like this if the script runs successfully
  
  ![code output](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-06%20at%2011.00.25.png)

### Step 5: Deploy the model as a web service 

Deploying the model as a web service enables one to use the model to make predictions about future transactions. To do this,
Run the following commands.
- `gunicorn --bind 0.0.0.0:9696 predict.py`
- From another terminal session from the cloned project directory, execute the following command to make a request to this web service
  ``` python request.py```
- You should get an output of the model prediction.

  ![prediction](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-06%20at%2020.30.41.png)
  
  > Note: For this request, I used a transaction detail from my test dataset.

  ### Step 6: Deploy the web service to a docker container.
  Pre-requisites: You should have Docker installed and running on the machine where you want to perform model deployment to Docker. Then run this command on your command line
  
 - `docker build -t "mlzoomcamp-project"`
   
   You should get an output like this to indicate you've successfully built a docker image from the docker file

   ![docker container](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-05%20at%2019.12.41.png)

 - Create a docker container from the image. The model prediction script as a web service will then be running inside this container. 
   Below command will create and run a docker container named mlzoomcamp-project (--name mlzoomcamp-project) running as a daemon i.e. 
   non-interactive mode (-d), mapping the port 9696 on the host to port 9696 on the container (-p 9696:9696 first port is host port, 
   second is container port. If you want to map a different port on host just change the first number), from image bank-td-prediction. 
   The container will be deleted if stopped or when you shut down your machine (--rm).
   
   `docker run --rm --name bank-td-cont -d -p 9696:9696 mlzoomcamp-project`
   
     You should get an output like this.

    ![output](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-06%20at%2010.18.40.png)

- Finally, Test sending some sample transaction data to the web service and see the results. For this, you can use the request.py 
  script provided as part of this repo, which has some sample transaction details  and can make a request to the Web app service.

  From another terminal session from the cloned project directory, execute the following command to make a request to this web service

  `python request.py`

  You should get an output like this

  ![prediction](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/Screen%20Shot%202023-07-06%20at%2020.30.41.png) 

### Step 7: Cloud deployment
Coming soon

If you have any questions, reach out to me via email at victorkingoshimua@gmail.com
