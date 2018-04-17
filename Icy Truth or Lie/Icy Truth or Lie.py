from __future__ import print_function
import random
import json
import os

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
    #if (event['session']['application']['applicationId'] != "amzn1.echo-sdk-ams.app.[unique-value-here]"):
     #   raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
        
        
# -------------- Events ------------------

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
    if intent_name == "ItIsStatementOneIntent":#ItIsStatementOneIntent
        return determine_score_1(intent, session) #change method to reflect(whether its )
    elif intent_name == "ItIsStatementTwoIntent":
        return determine_score_2(intent, session)
    elif intent_name == "ItIsStatementThreeIntent":
        return determine_score_3(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here        # -------------- Events ------------------

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
    if intent_name == "ItIsStatementOneIntent":#ItIsStatementOneIntent
        return determine_score_1() #change method to reflect(whether its )
    elif intent_name == "ItIsStatementTwoIntent":
        return determine_score_2()
    elif intent_name == "ItIsStatementThreeIntent":
        return determine_score_3()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
        

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


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    TRUTHS = ["a group of dolphins can kill a shark",\
    "sloths can fall to their death by accidentally grabbing their own leg instead of a tree branch",\
    "butterflies are cannibals",\
    "until they are six or seven months old, babies can breathe and swallow at the same time, adults cannot do that",\
    "vending machines kill more people than sharks do",\
    "lighters were invented before matches",\
    "mosquitos have teeth",\
    "bananas are berries, while strawberries are not"]

    LIES = ["octopuses have four hearts",\
    "eating foods that are rich in vitamin d helps increase the absorption of iron into the body",\
    "french is the second-most spoken language in north dakota",\
    "despite china's heavy internet censorship, it has faster internet speeds than the united states"]
    statements = [TRUTHS[random.randint(0, 7)],TRUTHS[random.randint(0, 7)],LIES[random.randint(0, 3)]]
    while(statements[0] == statements[1]):
        statements[1] = TRUTHS[random.randint(0, 7)]
    theLie = statements[2]
    os.environ['answerString']=theLie
    random.shuffle(statements)
    if(statements[0]==theLie):
        os.environ['answer'] = "0"
    elif  (statements[1]==theLie):
        os.environ['answer'] = "1"
    else:
        os.environ['answer'] = "2"

    speech_output = "Let's play Two Truths And a Lie! " \
                    "I will give you three statements, " \
                    "numbered from one to three." \
                    " Provide the number that corresponds to the "\
                    "statement that you believe is the lie." \
                    " Number one: "+ statements[0]+ ". Number two: "+ statements[1]+ ". Number three: "+ statements[2]+ ". Which statement is the lie?"
    should_end_session = False
    return build_response({}, build_speechlet_response(
        "welcome", speech_output, speech_output, False))

def determine_score_1():
    if os.environ['answer'] == "0":
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)+1)
        speech_output = "Congratulations! You determined the lie. " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."
    else:
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)-1)
        speech_output = "Sorry, you guessed wrong. The lie was Statement "+ os.environ['answer']+ ": "+ os.environ['answerString']+ ". " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."

    return build_response({}, build_speechlet_response(
        "score", speech_output, speech_output, False))
        

def determine_score_2():
    if os.environ['answer'] == "1":
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)+1)
        speech_output = "Congratulations! You determined the lie. " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."
    else:
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)-1)
        speech_output = "Sorry, you guessed wrong. The lie was Statement "+ os.environ['answer']+ ": "+ os.environ['answerString']+ ". " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."
    
    should_end_session = False
    return build_response({}, build_speechlet_response(
        "score", speech_output, speech_output, should_end_session))
        
    
def determine_score_3():
    if os.environ['answer'] == "2":
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)+1)
        speech_output = "Congratulations! You determined the lie. " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."
    else:
        i = os.environ['theLieScore']
        os.environ['theLieScore'] = str(int(i)-1)
        speech_output = "Sorry, you guessed wrong. The lie was Statement "+ os.environ['answer']+ ": "+ os.environ['answerString']+ ". " \
        "Your score is now "+ os.environ['theLieScore']+ ". Tell me to continue if you would like to play again."
    should_end_session = False
    return build_response({}, build_speechlet_response(
        "score", speech_output, speech_output, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thanks for playing. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# def create_favorite_color_attributes(favorite_color):
#     return {"favoriteColor": favorite_color}


# def set_color_in_session(intent, session):
#     """ Sets the color in the session and prepares the speech to reply to the
#     user.
#     """

#     card_title = intent['name']
#     session_attributes = {}
#     should_end_session = False

#     if 'Color' in intent['slots']:
#         favorite_color = intent['slots']['Color']['value']
#         session_attributes = create_favorite_color_attributes(favorite_color)
#         speech_output = "I now know your favorite color is " + \
#                         favorite_color + \
#                         ". You can ask me your favorite color by saying, " \
#                         "what's my favorite color?"
#         reprompt_text = "You can ask me your favorite color by saying, " \
#                         "what's my favorite color?"
#     else:
#         speech_output = "I'm not sure what your favorite color is. " \
#                         "Please try again."
#         reprompt_text = "I'm not sure what your favorite color is. " \
#                         "You can tell me your favorite color by saying, " \
#                         "my favorite color is red."
#     return build_response(session_attributes, build_speechlet_response(
#         card_title, speech_output, reprompt_text, should_end_session))


# def get_color_from_session(intent, session):
#     session_attributes = {}
#     reprompt_text = None

#     if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
#         favorite_color = session['attributes']['favoriteColor']
#         speech_output = "Your favorite color is " + favorite_color + \
#                         ". Goodbye."
#         should_end_session = True
#     else:
#         speech_output = "I'm not sure what your favorite color is. " \
#                         "You can say, my favorite color is red."
#         should_end_session = False

#     # Setting reprompt_text to None signifies that we do not want to reprompt
#     # the user. If the user does not respond or says something that is not
#     # understood, the session will end.
#     return build_response(session_attributes, build_speechlet_response(
#         intent['name'], speech_output, reprompt_text, should_end_session))
