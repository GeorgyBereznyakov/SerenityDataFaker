from data_gen import data_gen
from data_faker import data_faker
import time


class state_shift:
    def startRun(individual, ticket, hour, template, work_hours):
        foo = data_gen()
        faker = data_faker()
        currentTime = faker.currentTime()
        stateTime = faker.setBackwards(currentTime)
        foo.assign_tickets_yesterday(ticket, individual)
        for i in range(len(template)):
            if i + 1 == len(template):
                break
            foo.set_state(ticket, template[i], template[i + 1], stateTime)
            # foo.set_state2(ticket, template[i], template[i + 1])
            stateTime = faker.addTime(stateTime, hour)
            stateTime = faker.checkDay(stateTime)
            stateTime = faker.check_work_time(stateTime)
            time.sleep(10)
            # time.sleep(hour * 3600)
