
from __future__ import print_function
import os
import json

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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
def arrayOfGames(num):
    game = ["Truth or Lie: A game where players compete to most accurately decide which of the three given choices are invalid. The invocation for this game is: Icy Truth or Lie'",\
                "Scat time: A game where players team up to choose from what source each given sound would come from. The invocation for this game is 'Scat Time'",\
                "Charades: to be implemented",\
                "Story Grinder: to be implemented"]
    return game[num]

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Icebreakers with Alexa. " \
                    "We hope you have fun with your family and friends because of these. "\
                    "We offer an array of choices for you to pick from. Simply say next or previous to hear about the games that we offer."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "We offer an array of choices for you to pick from. Simply say next or previous to hear about the games that we offer."

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "We hope you have fun with your chosen game. " \
                    "Hope to talk to you soon! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()
def present(num):
    session_attributes = {}
    card_title = "Present"
    speech_output = arrayOfGames(num)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, speech_output, False))
def nextg():
    i = os.environ['gameNum']
    i = int(i) + 1
    if i == 4:
        i = 0
    os.environ['gameNum']=str(i)
    return present(i)
def prevg():
    i = os.environ['gameNum']
    i = int(i) - 1
    if i == -1:
        i = 3
    os.environ['gameNum']=str(i)
    return present(i)


def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    return nextg()

    if intent_name == "NetGam":
        return nextg()
    elif intent_name == "PresGam":
        return prevg()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    return ("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])



def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
