from data_gen import data_gen
from data_faker import data_faker
import time


class state_shift:
    def startRun(individual, ticket, hour, template):
        foo = data_gen()
        faker = data_faker()
        currentTime = faker.currentTime()
        stateTime = faker.setBackwards(currentTime)
        foo.assign_tickets(ticket, individual)
        for i in range(len(template)):
            if i + 1 == len(template):
                break
            foo.set_state(ticket, template[i], template[i + 1], stateTime)
            stateTime = faker.addTime(stateTime, hour)
            # time.sleep(hour * 3600)
            # currentTime = faker.addTimeString(currentTime, hour)
