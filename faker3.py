import pickle
from data_faker import data_faker
import threading
from state_shift import state_shift


def pickle_loader(filename):
    with open(filename, "rb") as handle:
        a = pickle.load(handle)
    return a


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
faker = data_faker()
individuals = pickle_loader("fake_users.pickle")
tickets = pickle_loader("fake_tickets.pickle")

threads = {}
for i in range(0, 3):
    threads.update(
        {
            i: threading.Thread(
                target=state_shift.startRun,
                args=(
                    individuals[f"ind_id{i}"],
                    tickets[f"ticket_id{i}"],
                    faker.genRandomHour(),
                    state_template[i],
                    8,
                ),
            )
        }
    )

for i in range(len(threads)):
    x = threads[i]
    x.start()
