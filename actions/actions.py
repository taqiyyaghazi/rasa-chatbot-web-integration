# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionTotalHTM(Action):

    def name(self) -> Text:
        return "action_total_htm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        total = int(tracker.get_slot('total')) 
        if total >= 1:
            message = "Total HTM untuk " + str(total) + " karya adalah Rp. " + str(total*30000)   
        else:
            message = "Berapa karya yang ingin anda daftarkan?"
        dispatcher.utter_message(text=message)

        return []
