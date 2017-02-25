"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import YACSwrapper
import json


# --------------- Data for API -----

##use environment variables here....

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session,should_refer_name=False):
    #if(should_refer_name):
    #    userid = session['attributes']['userid']
    #    output = characterInfo.getUsername(str(userid))+" "+output

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the yacs alexa app. Say help for a list of commands."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Welcome to the yacs alexa app. Say help for a list of commands."

    should_end_session = False
    #should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_help():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Help"
    speech_output = "Here's a list of commands: seats left, scheduling conflict."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Here's a list of commands: seats left, scheduling conflict."

    should_end_session = False
    #should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        "Help", speech_output, reprompt_text, should_end_session))

def get_specific_help(intent,session):
    session_attributes = {}
    card_title = "Specific Help"
    speech_output = ""
    try:
        if(intent['slots']['Help']['value']=="Scheduling Conflict"):
            speech_output = "Say scheduling conflict, and then four courses you want to take."
        elif(intent['slots']['Help']['value'] == "Seats Left"):
            speech_output = "Say how many seats left in course. Like how many seats are left in Introduction To Biology?"
    except KeyError:
        speech_output = "Say specific help"

    should_end_session = False
    #should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        "Specific help", speech_output, None, should_end_session))
    ##argument should be the specific function that you want help with.

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Goodbye. " \

    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))




def get_scheduling_conflict(intent,session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    should_end_session = True

    list_of_courses = [intent['slots']['Courseone']['value'],intent['slots']['Coursetwo']['value'],intent['slots']['Coursethree']['value'],intent['slots']['Coursefour']['value']]

    try:
        speech_output = YACSwrapper.getSchedulingConflict(list_of_courses)
    except KeyError:
        speech_output = "You must say 4 classes."

    return build_response(session_attributes, build_speechlet_response(
        "Get scheduling conflicts", speech_output, "anything else?", should_end_session))

def get_seats_left(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    should_end_session = True
    try:
        speech_output = YACSwrapper.getSeatsLeft(intent['slots']['Course']['value'])
    except KeyError:
        speech_output = "You must say a class to get seats left."
    return build_response(session_attributes, build_speechlet_response(
        "Get seats left", speech_output, "anything else?", should_end_session))




# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_help()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "SchedulingConflict":
        return get_scheduling_conflict(intent,session)
    elif intent_name == "SeatsLeft":
        return get_seats_left(intent,session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
