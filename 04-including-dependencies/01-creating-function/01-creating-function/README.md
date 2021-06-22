# Updating Function with Dependencies

## Install and Package Dependencies
1. We can also include dependencies into our function
2. First let's install python's `requests` library into a package directory
```
pip3 install --target ./package requests
```
3. Then let's create deployment package into that package directory
```
cd package
zip -r ../deployment.zip
cd ..
```
1. Then let's update our function to make a request call to a free Public API. This Public API will get us random useless facts. Check this in `lambda_function.py`
2. Let's add our function into the root of the deployment package
```
zip -g deployment.zip lambda_function.py
```
6. Finally let's update our function.
```
aws lambda update-function-code \
--function-name hello-cli-ninja \
--zip-file fileb://deployment.zip
```
7. And let's invoke it.
```
aws lambda invoke \
--function-name hello-cli-ninja \
--payload '{"first_name": "aditya"}' \
output.json
```
8. See the result
```
cat output.json
```