from data_gen import data_gen
from data_faker import data_faker
import time


class state_shift:
    def startRun(individual, ticket, hour, template, work_hours):
        foo = data_gen()
        faker = data_faker()
        currentTime = faker.currentTime()
        stateTime = faker.setBackwards(currentTime)
        j = 0
        for i in range(len(template)):
            if i + 1 == len(template):
                break
            foo.assign_tickets(ticket, individual[j], stateTime)
            j += 1
            if j == len(individual):
                j = 0
            foo.set_state(ticket, template[i], template[i + 1], stateTime)
            stateTime = faker.addTime(stateTime, hour)
            stateTime = faker.checkDay(stateTime)
            stateTime = faker.check_work_time(stateTime)
            time.sleep(10)
