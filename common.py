import boto3
from sabi import Sync
from dotenv import load_dotenv
from sabi import Clients
import os
import json


class Common:
    def __init__(self) -> None:
        load_dotenv()

    def invoke_lambda(name, params):
        lambda_client = boto3.client("lambda")

        return_value = lambda_client.invoke(FunctionName=name, InvocationType="RequestResponse", Payload=json.dumps(params))

        return json.loads(return_value["Payload"].read().decode())

    def get_jwt_token(payload):
        response = Common.invoke_lambda("jwt-generate", {"payload": payload, "issuer": "sabi", "audience": "api", "expire": 36000})
        return response["jwt"]

    def get_sync_client(company_integration_id):
        token = Common.get_jwt_token({"company_integration_id": company_integration_id})
        sabi = Sync(token, os.environ["api_host"])
        return sabi

    def get_clients_client():
        token = Common.get_jwt_token({})
        sabi = Clients(token, os.environ["api_host"])
        return sabi
