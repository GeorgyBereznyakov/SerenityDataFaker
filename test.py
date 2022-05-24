from data_gen import data_gen

test = data_gen()
individuals = test.gen_individual()
tickets = test.gen_tickets()
label = test.gen_label()

test.assign_tickets(tickets, individuals)
test.set_state(tickets)
test.set_ticket_labels(tickets, label)
test.get_tickets(tickets)
test.gen_field()
test.get_fields()
