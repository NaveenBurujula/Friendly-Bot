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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

professor_data = {
    "E Vijaya": {"ID": "P001", "Contact": "+1 234 567 8901", "Teaches": "Data Structures, DBMS, Software Engineering",
                 "Position": "Assistant Professor"},
    "Pooja Prasad": {"ID": "P002", "Contact": "+1 234 567 8902", "Teaches": "Computer Networks",
                     "Position": "Assistant Professor"},
    "Dr.Swathi": {"ID": "P003", "Contact": "+1 234 567 8903", "Teaches": "JAVA, Data structures",
                  "Position": "Assistant Professor"},
    "Raheera": {"ID": "P004", "Contact": "+1 234 567 8904", "Teaches": "SML", "Position": "Associate Professor"},
    "Dr.Sudhakar": {"ID": "P005", "Contact": "+1 234 567 8905", "Teaches": "Machine Learning",
                    "Position": "Assistant Professor"},
}

student_data = {
    "Burujula Naveen": {"ID": "21R11A0506", "Department": "CSE", "Contact": "+91 7671800324", "CGPA": "8.46",
                        "Email": "21r11a0506@gcet.edu.in"},
    "P Reena": {"ID": "21R11A0541", "Department": "CSE", "Contact": "+91 6305124575", "CGPA": "7.5",
                "Email": "21r11a0541@gcet.edu.in"},
    "Nithin Yadav": {"ID": "21R11A0532", "Department": "CSE", "Contact": "+91 9491460899", "CGPA": "7.2",
                     "Email": "21r11a0532@gcet.edu.in"},
    "Lasya": {"ID": "21R11A0503", "Department": "CSE", "Contact": "+91 9014755380", "CGPA": "8.3",
              "Email": "21r11a0503@gcet.edu.in"},
    "L Dhanya": {"ID": "21R11A0527", "Department": "CSE", "Contact": "+91 9390905132", "CGPA": "8.1",
                 "Email": "21r11a0527@gcet.edu.in"},
}


class ActionProfessorDetails(Action):

    def name(self) -> Text:
        return "action_professor_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        professor_name = tracker.get_slot("professor_name")
        if professor_name in professor_data:
            details = professor_data[professor_name]
            dispatcher.utter_message(
                text=f"Professor {professor_name}, ID: {details['ID']}, Contact: {details['Contact']}, Teaches: {details['Teaches']}, Working as: {details['Position']}")
        else:
            dispatcher.utter_message(text="Sorry, I don't have information about that professor.")
        return []


class ActionStudentDetails(Action):

    def name(self) -> Text:
        return "action_student_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        student_name = tracker.get_slot("student_name")
        if student_name in student_data:
            details = student_data[student_name]
            dispatcher.utter_message(
                text=f"Student {student_name}, ID: {details['ID']}, Department: {details['Department']}, Contact: {details['Contact']}, CGPA: {details['CGPA']}, Email: {details['Email']}")
        else:
            dispatcher.utter_message(text="Sorry, I don't have information about that student.")
        return []
