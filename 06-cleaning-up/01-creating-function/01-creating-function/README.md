# Cleaning up Resources

## Cleaning function
1. Let's delete our function
```
aws lambda delete-function --function-name hello-cli-ninja
```


## Cleaning roles
1. First let's detach the policy from the role
```
aws iam delete-role-policy --role-name lambda-ex-cli-ninja --policy-name AWSBasicLambdaExectionRole
```
2. Then let's delete the role
```
- aws iam delete-role --role-name lambda-ex-cli-ninja
```
