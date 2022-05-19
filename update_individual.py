import requests
import pickle
from dotenv import load_dotenv  # pipenv install python-dotenv
import os
import json


class updateIndividual:
    def __init__(self):
        load_dotenv()
        integration_id = os.environ["INTEGRATION_ID"]
        team_id = os.environ["TEAM_ID"]
        api_url = os.environ["URL"]

        f = open("fake_users", "rb")
        individual_id_dict = pickle.load(f)
        # print(individual_id_dict)
        f.close()

        self.url = f"{api_url}integrations/{integration_id}/individual"
        self.payload = {}

        # creates a payload using dict of all individuals
        # from file fake_users

        for i in range(len(individual_id_dict)):
            self.payload.update(
                {
                    f"payload{i}": {
                        "teams": [{"id": f"{team_id}"}],
                        "id": f"{individual_id_dict.get('id' + str(i))}",
                        "active": True,
                        "termination_date": "2023-05-05",
                    }
                }
            )

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['ACCESS_TOKEN']}",
        }

    def updateIndividual(self):
        for i in range(len(self.payload)):
            response = requests.post(self.url, json=self.payload.get(f"payload{i}"), headers=self.headers)
            print(json.dumps(json.loads(response.text), indent=2))
