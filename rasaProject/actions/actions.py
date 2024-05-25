# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionCoronaTracker(Action):
    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message["entities"]

        state = None
        for e in entities:
            if e["entity"] == "state":
                state = e["value"]
                break

        message = "Please Enter the correct state name"
        if state:
            for data in response["statewise"]:
                if data["state"].lower() == state.lower():
                    message = (
                        f"StateCode: {data['statecode']}, "
                        f"Active: {data['active']}, "
                        f"Confirmed: {data['confirmed']}, "
                        f"Death: {data['deaths']}, "
                        f"Recovered: {data['recovered']}, "
                        f"Last Updated: {data['lastupdatedtime']}"
                    )
                    break

        dispatcher.utter_message(text=message)
        return []

