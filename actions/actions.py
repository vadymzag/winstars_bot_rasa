# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []




# class ListUserDetails(Action):
#
#     def name(self) -> Text:
#         # Name of the action mentioned in the domain.yml file
#         return "action_list_user_details"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         # It will return array of entities
#         entities = tracker.latest_message['entities']
#
#         # Iterating through the array to retrieve the desired entity
#         for e in entities:
#             if e['entity'] == "user_name":
#                 entity_name = e['value']
#             elif e['entity'] == "city_name":
#                 entity_city = e['value']
#             elif e['entity'] == "designation":
#                 entity_designation = e['value']
#
#         dispatcher.utter_message(
#             template="utter_user_details",
#             name=entity_name,
#             city=entity_city,
#             designation=entity_designation
#         )
#
#         return []
