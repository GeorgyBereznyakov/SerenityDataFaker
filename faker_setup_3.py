import pickle
from data_faker import data_faker
from data_gen import data_gen
import threading
from state_shift import state_shift
import sys

sys.path.append("/home/workspace/src/serenity_testing/")

from get_ticket_num_faker import get_ticket_number


faker = data_faker()
gen = data_gen()

state1 = "Backlog"
state2 = "Scheduled"
state3 = "In Progress"
state4 = "Review"
state5 = "Deploy"
state6 = "Done"

state_template = {
    0: {
        0: state1,
        1: state2,
        2: state3,
        3: state4,
        4: state5,
        5: state6,
    },
    1: {
        0: state1,
        1: state3,
        2: state4,
        3: state3,
        4: state4,
        5: state5,
        6: state6,
    },
    2: {
        0: state1,
        1: state2,
        2: state1,
        3: state2,
        4: state3,
        5: state4,
        6: state5,
        7: state6,
    },
    3: {
        0: state1,
        1: state2,
        2: state3,
        3: state1,
        4: state2,
        5: state3,
        6: state4,
        7: state3,
        8: state4,
        9: state5,
        10: state6,
    },
    4: {
        0: state1,
        1: state2,
        2: state3,
        3: state4,
        4: state5,
        5: state4,
        6: state3,
        7: state4,
        8: state5,
        9: state6,
    },
    5: {
        0: state1,
        1: state2,
        2: state3,
        3: state2,
        4: state3,
        5: state4,
        6: state3,
        7: state4,
        8: state5,
        9: state6,
    },
    6: {
        0: state1,
        1: state2,
        2: state3,
        3: state4,
        4: state1,
        5: state2,
        6: state3,
        7: state4,
        8: state3,
        9: state4,
        10: state5,
        11: state6,
    },
    7: {
        0: state1,
        1: state2,
        2: state3,
        3: state4,
        4: state2,
        5: state3,
        6: state4,
        7: state5,
        8: state6,
    },
    8: {
        0: state1,
        1: state2,
        2: state3,
        3: state4,
        4: state3,
        5: state2,
        6: state1,
        7: state2,
        8: state3,
        9: state4,
        10: state5,
        11: state6,
    },
    9: {
        0: state1,
        1: state2,
        2: state1,
        3: state2,
        4: state1,
        5: state2,
        6: state3,
        7: state2,
        8: state3,
        9: state4,
        10: state3,
        11: state4,
        12: state5,
        13: state6,
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

for i in range(ticket_amount, tickets_to_add):
    time_per_shift = faker.genRandomInt(1, 8)
    time_map.update({i: time_per_shift})
    ticket_template, state_index = gen.pick_template(state_template)
    state_map.update({i: ticket_template})
    individual_amount = faker.genRandomInt(1, 5)
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
