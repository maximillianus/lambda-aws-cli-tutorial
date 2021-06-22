# Invoke Function

## Invoking Function
1. Let's try to invoke our lambda function and pass the parameter values. This parameter will need to be outputted to a file
```
aws lambda invoke \
--function-name hello-cli-ninja \
--payload '{"first_name": "aditya"}' \
output.json
```
2. Let's see the JSON output
```
cat output.json
```