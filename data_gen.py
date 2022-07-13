from common import Common
from data_faker import data_faker
import time
import json
import random
import pickle


class data_gen:
    def __init__(self):
        self.faker = data_faker()
        self.sabi_client = Common.get_clients_client()
        foo = self.sabi_client.integrations("clubhouse")
        # print(foo)
        for i in range(len(foo)):
            if foo[i]["company_name"] == "SerenityTestAutomation":
                x = foo[i]["company_integration_id"]
                self.sabi_sync = Common.get_sync_client(x)
                break

    def pickle_loader(self, filename):
        with open(filename, "rb") as handle:
            a = pickle.load(handle)
            handle.close()
        return a

    def gen_individual(self):
        individual_id = {}
        for i in range(0, 20):
            payload = [
                {
                    "id": f"{i + 1}",
                    "name": self.faker.genName(),
                    "email": self.faker.genEmail(),
                    "avatar_url": self.faker.genUrl(),
                    "active": "yes",
                    "json": "{}",
                }
            ]
            response = self.sabi_sync.save_individuals(payload)
            individual_id.update({f"ind_id{i}": payload[0]["id"]})
            # print(response)
            # print(individual_id)

        return individual_id

    def gen_states(self):
        state_name = {
            0: "Backlog",
            1: "Scheduled",
            2: "In Progress",
            3: "Review",
            4: "Deploy",
            5: "Done",
        }
        type_name = {
            0: "ignore",
            1: "to do",
            2: "in progress",
            3: "to do",
            4: "to do",
            5: "done",
        }
        for i in range(0, 6):
            payload = [
                {
                    "id": state_name[i],
                    "name": state_name[i],
                    "flow": "DataFaker",
                    "position": i,
                    "type": type_name[i],
                }
            ]
            response = self.sabi_sync.save_states(payload)
            print(response)

        return state_name

    def gen_tickets(self, payload):
        ticket_id = {}
        response = self.sabi_sync.save_tickets(payload)
        for i in range(len(payload)):
            ticket_id.update({i: payload[i]["ticket_id"]})

        return ticket_id

    def assign_tickets_yesterday(self, ticket_id, individual_id):
        time = self.faker.currentTime()
        yTime = self.faker.setBackwards(time)
        payload = [
            {
                "ticket_id": ticket_id,
                "individual_id": individual_id,
                "add_or_remove": "added",
                "datetime": yTime,
            }
        ]
        response = self.sabi_sync.save_ticket_assignments(payload)
        print(response)
        print(f"Ticket {ticket_id} assigned to Individual {individual_id} at {yTime}")

    def assign_tickets(self, payload):
        response = self.sabi_sync.save_ticket_assignments(payload)

    def set_state(self, payload):
        response = self.sabi_sync.save_ticket_status_changes(payload)

    def set_state2(self, ticket_id, currentState, nextState):
        payload = [
            {
                "ticket_id": ticket_id,
                "from_state": currentState,
                "to_state": nextState,
                "datetime": self.faker.currentTime(),
            }
        ]
        response = self.sabi_sync.save_ticket_status_changes(payload)
        print(response)
        print(f"Ticket {ticket_id} changed State from {currentState} to {nextState} at Time {self.faker.currentTime()}")

    def testing_set_state(self, payload):
        response = self.sabi_sync.save_ticket_status_changes(payload)
        print(response)

    def get_tickets(self, ticket_id):
        for i in range(len(ticket_id)):
            response = self.sabi_sync.get_ticket(ticket_id[f"ticket_id{i}"])
            print(response)

    def get_ticket(self, ticket_id):
        response = self.sabi_sync.get_ticket(ticket_id)
        print(response)

    def get_fields(self):
        response = self.sabi_sync.get_fields()
        print(response)

    def gen_field(self):
        payload = [
            {
                "id": "foo",
                "name": "foo",
                "is_custom": "yes",
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
                    "datetime": self.faker.currentTime(),
                }
            ]
            response = self.sabi_sync.save_ticket_labels(payload)
            print(response)

    def gen_project(self):
        payload = [
            {
                "project_id": "1",
                "name": "Faker",
                "short_name": "fa",
                "description": "blah blah",
                "json": "{}",
            }
        ]
        response = self.sabi_sync.save_projects(payload)
        print(response)

    def pick_template(self, state_template):
        index, ticket_template = random.choice(list(state_template.items()))
        return ticket_template, index

    def pick_individual(self, num):
        individuals = self.pickle_loader("fake_users.pickle")
        pop_individuals = individuals
        ticket_individuals = {}

        for i in range(num):
            choice = random.choice(list(pop_individuals.keys()))
            temp = pop_individuals[choice]
            ticket_individuals.update(
                {i: temp},
            )
            pop_individuals.pop(choice)
        return ticket_individuals

    def build_description(self, template, individuals, index, time):
        description = f"Ticket State Template {index}: "

        for i in range(len(template)):
            description += template[i]
            description += "->"

        description += f" Time Per State: {time} hours, "

        description += " Individuals assigned: "

        for i in range(len(individuals)):
            description += individuals[i]
            description += ", "

        return description

    def batch_payload(self, payload, temp):
        payload.append(temp)
        return payload

    def build_ticket_payload(self, num, description, payload):
        link = self.faker.genBothify("???-####")
        time = self.faker.currentTime()
        yTime = self.faker.setBackwards(time)
        temp = {
            "ticket_id": f"{num}",
            "name": f"ticket{num}",
            "description": description,
            "parent_id": "0",
            "created_at": yTime,
            "deleted": "no",
            "estimate": self.faker.genInt(1, 5, 1),
            "type": "bug",
            "project_id": "a2Rwz63dzvXLYxmZ",
            "link": f"https://test_comp.atlassian.net/browse/{link}",
        }
        return self.batch_payload(payload, temp)

    def build_assign_payload(self, ticket, individual, stateTime, payload):
        temp = {
            "ticket_id": ticket,
            "individual_id": individual,
            "add_or_remove": "added",
            "datetime": stateTime,
        }
        return self.batch_payload(payload, temp)

    def build_state_payload(self, ticket, currentState, nextState, time, payload):
        temp = {
            "ticket_id": ticket,
            "from_state": currentState,
            "to_state": nextState,
            "datetime": time,
        }
        return self.batch_payload(payload, temp)
