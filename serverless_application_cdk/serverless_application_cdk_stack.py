from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as httpIntegration
)
from constructs import Construct


class ServerlessApplicationCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        backendLambda = _lambda.Function(
            self,
            "beckendFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("lambda"),
            handler="backend-lambda.lambda_handler",    
        )

        http_api = apigwv2.HttpApi(self, "serverless-application-api")
        backend_lambda_integration = httpIntegration.HttpLambdaIntegration(
            "backEndIntegration", backendLambda)
        http_api.add_routes(
            path='/',
            methods=[apigwv2.HttpMethod.GET],
            integration=backend_lambda_integration
        )
