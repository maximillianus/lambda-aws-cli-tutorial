# Publishing Function Version

## Publishing function
1. We can do a version control in our Lambda function
2. To do that let's publish a version of our lambda function
```
aws lambda publish-version --function-name hello-cli-ninja
```
3. Then let's try to invoke that function version by specifying the `qualifier` parameter
```
aws lambda invoke \
--function-name hello-cli-ninja \
--payload '{"first_name": "aditya"}' \
--qualifier 1 \
output.json
```
