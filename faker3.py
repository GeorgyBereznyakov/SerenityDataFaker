import pickle
from data_faker import data_faker
from data_gen import data_gen
import threading
from state_shift import state_shift
import sys

sys.path.append("/home/workspace/src/serenity_testing/")

from get_ticket_num_faker import get_ticket_number

""" 
todo: 
- add code for custom work day
- batch tickets
- 
"""


faker = data_faker()
gen = data_gen()


state_template = {
    0: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Review",
        4: "Deploy",
        5: "Done",
    },
    1: {
        0: "Backlog",
        1: "In Progress",
        2: "Review",
        3: "In Progress",
        4: "Review",
        5: "Deploy",
        6: "Done",
    },
    2: {
        0: "Backlog",
        1: "Scheduled",
        2: "Backlog",
        3: "Scheduled",
        4: "In Progress",
        5: "Review",
        6: "Deploy",
        7: "Done",
    },
    3: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Backlog",
        4: "Scheduled",
        5: "In Progress",
        6: "Review",
        7: "In Progress",
        8: "Review",
        9: "Deploy",
        10: "Done",
    },
    4: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Review",
        4: "Deploy",
        5: "Review",
        6: "In Progress",
        7: "Review",
        8: "Deploy",
        9: "Done",
    },
    5: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Scheduled",
        4: "In Progress",
        5: "Review",
        6: "In Progress",
        7: "Review",
        8: "Deploy",
        9: "Done",
    },
    6: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Review",
        4: "Backlog",
        5: "Scheduled",
        6: "In Progress",
        7: "Review",
        8: "In Progress",
        9: "Review",
        10: "Deploy",
        11: "Done",
    },
    7: {
        0: "Backlog",
        1: "Scheduled",
        2: "In Progress",
        3: "Review",
        4: "Scheduled",
        5: "In Progress",
        6: "Review",
        7: "Deploy",
        8: "Done",
    },
}

# Gets number of tickets in system (0 if none)
foo = get_ticket_number()
ticket_amount = foo.get_num_tickets()
tickets_to_add = ticket_amount + 1000
tickets = []
state_map = {}
individuals_map = {}
time_map = {}
# threads = {}
# j = 0
for i in range(ticket_amount, tickets_to_add):
    time_per_shift = faker.genRandomHour()
    time_map.update({i: time_per_shift})
    ticket_template, state_index = gen.pick_template(state_template)
    state_map.update({i: ticket_template})
    individual_amount = faker.genRandomInt()
    ticket_individuals = gen.pick_individual(individual_amount)
    individuals_map.update({i: ticket_individuals})
    description = gen.build_description(
        ticket_template,
        ticket_individuals,
        state_index,
        time_per_shift,
    )
    tickets = gen.build_ticket_payload(i, description, tickets)
ticket_id = gen.gen_tickets(tickets)

state_shift.startRun(individuals_map, ticket_id, time_map, state_map, gen, faker, ticket_amount)
