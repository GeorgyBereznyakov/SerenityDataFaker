from common import Common
from data_faker import data_faker
from get_individuals import getIndividuals
from update_individual import updateIndividual
import time
import json


faker = data_faker()
sabi_client = Common.get_clients_client()
integrations = sabi_client.integrations("clubhouse")
int_id = integrations[8]["company_integration_id"]
sabi_sync = Common.get_sync_client(238)

# temp testing
sabi_api = getIndividuals()

for i in range(0, 10):
    payload = [
        {
            "id": faker.genInt(1, 12, 1),
            "name": faker.genName(),
            "email": faker.genEmail(),
            "avatar_url": faker.genUrl(),
            "active": True,
            "json": "{}",
        }
    ]
    response = sabi_sync.save_individuals(payload)
    print(response)


sabi_api.getIndividuals()
update_individual = updateIndividual()
update_individual.updateIndividual()

for i in range(0, 10):
    payload = [
        {
            "ticket_id": f"{i}",
            "name": f"ticket{i}",
            "description": faker.genDescription(),
            "parent_id": "12",
            "created_at": faker.genDate(),
            "deleted": False,
            "estimate": faker.genInt(1, 5, 1),
            "type": "bug",
            "project_id": "a2Rwz63dzvXLYxmZ",
            "json": "{}",
        }
    ]
    response = sabi_sync.save_tickets(payload)
    print(response)
