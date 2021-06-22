# Updating Function

## Updating Function
1. Our Lambda function can track memory usage and execution time through the use of `context` environment variable.
2. Let's update our function with codes to see memory usage and execution time. Check this in `lambda_function.py` file.
3. Then let's add our function into the deployment package
```
zip deployment.zip lambda_function.py
```
4. And finally let's update our function
```
aws lambda update-function-code \
--function-name hello-cli-ninja \
--zip-file fileb://deployment.zip

```
