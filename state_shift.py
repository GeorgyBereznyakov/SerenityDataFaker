from data_gen import data_gen
from data_faker import data_faker
import time


class state_shift:
    def startRun(individual, ticket, hour, template, gen, faker, ticket_amount):
        currentTime = faker.currentTime()
        stateTime = faker.setBackwards(currentTime)
        assign_ind_payload = []
        state_change_payload = []
        j = 0
        for i in range(ticket_amount, len(ticket)):
            for j in range(len(individual[i])):
                assign_ind_payload = gen.build_assign_payload(
                    ticket[i],
                    individual[i][j],
                    stateTime,
                    assign_ind_payload,
                )
            if j == len(individual[i]):
                j = 0
        j = 0
        for i in range(ticket_amount, len(ticket)):
            for j in range(len(template[i])):
                if j + 1 == len(template[i]):
                    j = 0
                    break
                state_change_payload = gen.build_state_payload(
                    ticket[i],
                    template[i][j],
                    template[i][j + 1],
                    stateTime,
                    state_change_payload,
                )

        gen.assign_tickets(assign_ind_payload)
        gen.set_state(state_change_payload)
        # if i + 1 == len(template):
        #     break
        # gen.assign_tickets(ticket, individual[j], stateTime)
        # j += 1
        # if j == len(individual):
        #     j = 0
        # gen.set_state(ticket, template[i], template[i + 1], stateTime)
        # stateTime = faker.addTime(stateTime, hour)
        # stateTime = faker.checkDay(stateTime)
        # stateTime = faker.check_work_time(stateTime)
