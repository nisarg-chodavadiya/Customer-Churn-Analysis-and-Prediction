# Customer-Churn-Analysis-and-Prediction
Problem Statement:
Recommend the steps to retain existing telecom customers. In the industry retaining customers is going challenging day by day and acquire new customers is even draining so retaining the existing customers is highly worths every effort than acquiring new customers.
Know the customer behavior and recommend the steps to retain existing customers and build the model to know which existing customers may leave.
1. Customer Analysis -- Steps to Retain Customers -- Hypothesis test
2. Predictive Model
3. Web App in FastAPI

### Data
![image](https://user-images.githubusercontent.com/75474944/142570115-43ccc4b4-eae5-4562-a4a7-d11f074093ce.png)

## 1. Customer Analysis
All customers are divided into two segments from data usage and analysis of all customer attributes for each segment analyzed.
Some of the Visualizations are below.

![image](https://user-images.githubusercontent.com/75474944/134847344-ac9847bd-9b15-4c55-bad6-eb5566c4383d.png)
![image](https://user-images.githubusercontent.com/75474944/134847191-22dbd991-06f0-4d62-a91a-2966765bd9bd.png)
![image](https://user-images.githubusercontent.com/75474944/134847242-5811a3be-b7af-4fe7-ab75-5f91d775d9bd.png)
![image](https://user-images.githubusercontent.com/75474944/134847273-d4676d6a-d7ae-4e9d-b247-8ef59c93e4a4.png)

## Customer Segmentation
![image](https://user-images.githubusercontent.com/75474944/137465838-d3aba881-9b8c-497b-be8d-62f50748db20.png)
![image](https://user-images.githubusercontent.com/75474944/137465858-152958e7-b1c7-4dc2-9087-a956d1a7781f.png)

## Steps to Retain Customers
* More Customer Service calls mean the customer is more prone to churn.
* Optimize the price of talk time for segment 1 customers.
* Introduce a data plan to those customers who are using data without data plans ASAP.
* Introduce exciting data plans to segment 1 customers.
* If the possible optimizing price of data plans can retain segment 2 customers also.

## Hypothesis Test
**Null Hypothesis:** Which customers are using data without subscribing to data plan are more prone to churn.

**Alternate Hypothesis:** Which customers are using data without subscribing to data plan are not prone to churn.

**Permutation Experiments**
* In this test random sample of 20 customers will be taken.
* That 20 customers will be in two groups.
* Group2: Customers which are using data without subscribing data plan.
* Group1: All remaining Customers which are not in Group2.
* Find the churn ratio in both groups.

**Test Result**
* ~70% of experiments are in favor of the null hypothesis.
* Null hypothesis accepted.
* All conclusions on customer analysis are going right.

## 2. Predictive Model
Comparison of different algorithms

![image](https://user-images.githubusercontent.com/75474944/140018545-31777cc8-3b5d-437a-b6bf-d94095a1b315.png)

### Machine Learning Models
* Random Forest, Gradientboost are best.
* Gradientboost, decision tree, KNN are hyperparameter tuned. Random forest is not hyperparameter tuned.

## 3. FastAPI 
API: FastAPI, uvicorn.
