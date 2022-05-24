from common import Common
from data_faker import data_faker
import time
import json


class data_gen:
    def __init__(self):
        self.faker = data_faker()
        self.sabi_client = Common.get_clients_client()
        self.sabi_sync = Common.get_sync_client(242)

    def gen_individual(self):
        individual_id = {}
        for i in range(0, 10):
            payload = [
                {
                    "id": self.faker.genInt(1, 12, 1),
                    "name": self.faker.genName(),
                    "email": self.faker.genEmail(),
                    "avatar_url": self.faker.genUrl(),
                    "active": True,
                    "json": "{}",
                }
            ]
            response = self.sabi_sync.save_individuals(payload)
            individual_id.update({f"ind_id{i}": payload[0]["id"]})
            print(response)
            # print(individual_id)

        return individual_id

    def gen_tickets(self):
        ticket_id = {}
        for i in range(0, 10):
            link = self.faker.genBothify("???-####")
            payload = [
                {
                    "ticket_id": f"{i}",
                    "name": f"ticket{i}",
                    "description": self.faker.genDescription(),
                    "parent_id": "12",
                    "created_at": self.faker.genDate(),
                    "deleted": False,
                    "estimate": self.faker.genInt(1, 5, 1),
                    "type": "bug",
                    "project_id": "a2Rwz63dzvXLYxmZ",
                    "link": f"https://test_comp.atlassian.net/browse/{link}",
                }
            ]
            response = self.sabi_sync.save_tickets(payload)
            ticket_id.update({f"ticket_id{i}": payload[0]["ticket_id"]})
            print(response)
            # print(ticket_id)

        return ticket_id

    def assign_tickets(self, ticket_id, individual_id):
        for i in range(0, 10):
            payload = [
                {
                    "ticket_id": ticket_id[f"ticket_id{i}"],
                    "individual_id": individual_id[f"ind_id{i}"],
                    "add_or_remove": "added",
                    "datetime": "2022-05-23 13:32:30.48+00",
                }
            ]
            response = self.sabi_sync.save_ticket_assignments(payload)
            print(response)

    def set_state(self, ticket_id):
        for i in range(len(ticket_id)):
            payload = [
                {
                    "ticket_id": ticket_id[f"ticket_id{i}"],
                    "from_state": "State A",
                    "to_state": "State B",
                    "datetime": "2022-05-24 12:30:00.00+00",
                }
            ]
            response = self.sabi_sync.save_ticket_status_changes(payload)
            print(response)

    def get_tickets(self, ticket_id):
        for i in range(len(ticket_id)):
            response = self.sabi_sync.get_ticket(ticket_id[f"ticket_id{i}"])
            print(response)

    def get_fields(self):
        response = self.sabi_sync.get_fields()
        print(response)

    def gen_field(self):
        payload = [
            {
                "id": "foo",
                "name": "foo",
                "is_custom": True,
                "type": "text",
                "json": "{}",
            }
        ]
        response = self.sabi_sync.save_fields(payload)
        print(response)

    def gen_label(self):
        label = {}
        payload = [
            {
                "id": "test",
                "name": "test",
            }
        ]
        response = self.sabi_sync.save_labels(payload)
        print(response)
        return payload

    def set_ticket_labels(self, ticket_id, label_id):
        for i in range(len(ticket_id)):
            payload = [
                {
                    "ticket_id": ticket_id[f"ticket_id{i}"],
                    "label_id": label_id[0]["id"],
                    "add_or_remove": "added",
                    "datetime": "2022-05-24 13:30:00.00+00",
                }
            ]
            response = self.sabi_sync.save_ticket_labels(payload)
            print(response)
