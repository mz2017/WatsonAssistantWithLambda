# Sample Watson Assistant Skill With AWS Lambda Function

### Instructions:
#### AWS instructions
1. Login to AWS
2. Open Lambda service, and create a new Python Lambda function
3. Copy and paste the content of the lambda_function.py file to the Lambda action in the browser
4. Create an AWS API with HTTP to access the Lambda action. For demo purposes, no security is required

#### Watson assistant setup instructions
1. Login to IBM cloud
2. Create a Watson Assistant service
3. Create a new SKill by importing the JSON file provided in this repository
4. Open the dialogue and update the Webhook URL to match the AWS API for the Lambda function
5. Test the Skill using any of the following quesitons.

#### Sample questions:
- Help
- Show me sales orders for IBM
- What inventory do we have
- Where do we have iPhone
- SHow me inventory at store

