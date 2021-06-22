# Creating Function

## Creating Role
1. First we need to create an execution role to be used by our Lambda function
2. We also need to attach trust policy to our execution role
```
aws iam create-role \
--role-name lambda-ex-cli-ninja \
--assume-role-policy-document file://iam-role-trust-policy.json
```
2. We need to attach policy to our role so our Lambda can call the necessary services such as Cloudwatch

```
aws iam attach-role-policy \
--role-name lambda-ex \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```


## Creating Lambda Function
1. Then we can create our Lambda function (in Python)
2. Create the deployment package for our Lambda function
```
zip deployment.zip lambda_function.py
```
3. Then let's run the CLI command to create the function
```
aws lambda create-function \
--function-name hello-cli-ninja \
--zip-file fileb://deployment.zip \
--handler lambda_function.lambda_handler \
--runtime python3.8 \
--role arn:aws:iam::860873776111:role/lambda-ex-cli-ninja
```


## Getting Lambda Function
1. Let's try to get our lambda function to see if we created the function successfully
```
aws lambda get-function \
--function-name hello-cli-ninja
```