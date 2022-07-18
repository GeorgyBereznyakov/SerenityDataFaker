from data_gen import data_gen
import pickle


def pickle_dumper(filename, dict):
    with open(filename, "wb") as handle:
        pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


test = data_gen()
individuals = test.gen_individual()
pickle_dumper("fake_users.pickle", individuals)
states = test.gen_states()
