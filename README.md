![Credit card image gotten from usplash.com](https://github.com/cyberholics/mlzoomcamp-midterm-project/blob/main/images/nathana-reboucas-ND5HWK6Ivrg-unsplash.jpg)

# Machine-Learning-zoomcamp-Midterm-project

This repo contains project work I carried out as the midterm project in the [mlzoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp).  The course was organised by [Alexy Grigorev](https://github.com/alexeygrigorev).

## Table of contents

- [1. About the project](#topic1)
- [2. Project files and folder explained](#topic2)
- [Topic 3](#topic3)


<h2 id="topic1"> 1. About the project</h2>

Credit card fraud can be defined as any fraud or theft that involves a credit card. Credit card fraud aims to purchase goods or steal money with someone else credit account. Advance in modern-day technology has created more room for credit card fraud. Since the invention of online purchases, perpetrators no longer need a physical card to make an unauthorized purchase. Additionally, electronic databases containing credit card data can get hacked or crash on their own, releasing customers' credit card information. These electronic database hacks put the security of many accounts at risk at once.

Common forms of credit card fraud include:

- Lost or stolen cards are used without their owner's permission.

- Credit cards are 'skimmed,' where the card is cloned or copied using a special swipe machine to create a duplicate.

- Card details, such as the card number, cardholder name, date of birth, and address, are stolen from online databases or through email scams. These stolen details are then sold and utilized for fraud on the internet or over the phone. This type of fraud is often referred to as 'card-not-present' fraud.

- Fraudulent applications are made in someone else's name for a new credit card, without the person's knowledge or consent.

The goal of this project is to build a fraud detection system using machine learning. This system will have the ability to classify an online credit card transaction as fraudulent or not fraudulent based on the transaction details. The machine learning model will learn from past credit card transaction data and use the patterns it learns from the data to identify if a new transaction is fraudulent or not. Furthermore, the model will be hosted as a web service that accepts credit card transaction details in a JSON data format and returns a prediction of whether the transaction is fraudulent or not. Deploying this model as a web service will be beneficial to financial institutions, banks, or online stores as they can easily feed transaction details to the machine learning system and the model will return its prediction. This can help dectecting in potential fraud in trade and therefore get the transaction flagged and declined. By identifying potential instances of fraud, companies can take steps to prevent fraudulent activity from occurring, which can save them a significant amount of money loss.

<h2 id="topic2"> 2. Project files and folder explained</h2>

 ### Data
 > This folder gives you access to the data used in this project
### Images 
 > This is a folder of images I used in this project
### credit card fraud detection.ipynb
 > This is a Jupyter notebook that contains the codes I used for data preparation, EDA(Explanatory data analysis), model training/selection, and hyperparameter tuning.
