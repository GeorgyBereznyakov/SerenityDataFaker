import pickle
from data_faker import data_faker
from data_gen import data_gen
import threading
from state_shift import state_shift

""" 
todo: 
- get total tickets in company
- add more templates
- add code for custom work day
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

threads = {}
j = 0
for i in range(16, 24):
    ticket_template, state_index = gen.pick_template(state_template)
    ticket_individuals = gen.pick_individual()
    description = gen.build_description(ticket_template, ticket_individuals, state_index)
    ticket = gen.gen_tickets(i, description)
    threads.update(
        {
            j: threading.Thread(
                target=state_shift.startRun,
                args=(
                    ticket_individuals,
                    ticket,
                    faker.genRandomHour(),
                    ticket_template,
                    8,
                ),
            )
        }
    )
    j += 1

for i in range(len(threads)):
    x = threads[i]
    x.start()
