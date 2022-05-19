from common import Common

sabi_client = Common.get_clients_client()

print(sabi_client.integrations("clubhouse"))
