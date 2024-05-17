import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_application_cdk.serverless_application_cdk_stack import ServerlessApplicationCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_application_cdk/serverless_application_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessApplicationCdkStack(app, "serverless-application-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
