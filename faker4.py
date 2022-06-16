from data_gen import data_gen
import pickle


foo = data_gen()
with open("fake_tickets.pickle", "rb") as handle:
    tickets = pickle.load(handle)

foo.get_tickets(tickets)
