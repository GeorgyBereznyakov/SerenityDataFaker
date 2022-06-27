import pickle
from data_faker import data_faker
from data_gen import data_gen
import threading
from state_shift import state_shift




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
}

threads = {}

for i in range(0, 8):
    ticket_template, state_index = gen.pick_template(state_template)
    ticket_individuals = gen.pick_individual()
    description = gen.build_description(ticket_template, ticket_individuals, state_index)
    ticket = gen.gen_tickets(i, description)
    threads.update(
        {
            i: threading.Thread(
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

for i in range(len(threads)):
    x = threads[i]
    x.start()
