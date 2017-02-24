# alexatutorial
This is a tutorial for creating a basic Alexa skill. (No Alexa Required)


Go on https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/select-blueprint

Skill that interfaces with a 3rd party service with an api key and a rest api.


Will use YACS as an example. It has a good REST API service, and can return useful information.

What if we could interact with YACS on a vocal basis?

Goal: 

List a single course to alexa, and it will tell you how many seats are in all sections.

List courses to alexa skill, and it will tell you if there are any possible schedules.


API skills kit.
- Create a name for your app, to get started.

- Create Intents JSON file.

- Define Slot Types.

- Add List of possible values for slots.



Amazon Web Services Backend.
-Get lambda_function.py setup.
-Create separate file to import.


Extra details:

Build tool to create all the files necessary in Alexa skills kit (as slot value possibilities can be dynamic, courses change every year)

