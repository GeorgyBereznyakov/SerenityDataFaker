import requests
from dotenv import load_dotenv
import pickle
import os
import json


class getIndividuals:
    def __init__(self):
        load_dotenv()
        integration_id = os.environ["INTEGRATION_ID"]
        api_url = os.environ["URL"]
        self.url = f"{api_url}integrations/{integration_id}/individuals?only_active=yes"
        print(self.url + "\n")
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {os.environ['ACCESS_TOKEN']}",
        }

    def getIndividuals(self):
        response = requests.get(self.url, timeout=None, headers=self.headers)

        intermediate = json.loads(response.text)

        individual = intermediate["data"]
        ind_id = {}

        # creates dict of all individual ids
        for i in range(len(individual)):
            ind_id.update({f"id{i}": individual[i]["id"]})

        # stores dict in file fake_users
        f = open("fake_users", "wb")
        pickle.dump(ind_id, f)
        f.close()
