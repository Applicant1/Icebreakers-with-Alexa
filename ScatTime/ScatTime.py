from __future__ import print_function
from random import randint
import json
import os


def getWinner(num):
    congrats = ["Wow, you're better than I thought. ","You're still irredeemable. ","Wait how did you get that? ","I knew you were amazing! ","Keep going, I'm your biggest fan! "]
    return congrats[num]
def getLoser(num):
    loser = ["Wow, you really do suck. ","Um, it's ok you'll get it next time! ","Hey, you'll still carry the team later. ",\
         "How did you get that one wrong... ", "G G, this feeder... " ]
    return loser[num]
def getMusic(num):
    music = ["<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_cat_angry_meow_1x_02.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_crow_caw_1x_02.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_elephant_03.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_sheep_bleat_01.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/cartoon/amzn_sfx_boing_short_1x_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_glasses_clink_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_silverware_clank_02.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_swoosh_fast_1x_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_faucet_running_02.mp3'/>","other",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_footsteps_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_vacuum_on_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/human/amzn_sfx_crowd_boo_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/human/amzn_sfx_large_crowd_cheer_03.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/magic/amzn_sfx_ghost_spooky_01.mp3'/>","other",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/nature/amzn_sfx_rain_on_roof_01.mp3'/>","other"]
    return music[num]
def getCat(num):
    music = ["<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_cat_angry_meow_1x_02.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_crow_caw_1x_02.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_elephant_03.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/animals/amzn_sfx_sheep_bleat_01.mp3'/>","animal",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/cartoon/amzn_sfx_boing_short_1x_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_glasses_clink_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_silverware_clank_02.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/foley/amzn_sfx_swoosh_fast_1x_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_faucet_running_02.mp3'/>","other",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_footsteps_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/home/amzn_sfx_vacuum_on_01.mp3'/>","machine",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/human/amzn_sfx_crowd_boo_01.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/human/amzn_sfx_large_crowd_cheer_03.mp3'/>","human",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/magic/amzn_sfx_ghost_spooky_01.mp3'/>","other",\
         "<audio src='https://s3.amazonaws.com/ask-soundlibrary/nature/amzn_sfx_rain_on_roof_01.mp3'/>","other"]
    return music[num]
def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def get_welcome_response():
    session_attributes = {}
speech_output = "Hello humans! Let's play Scat Time! " \
                    "I will play a sound" \
                    " produced by either an animal, human, tool, or some other category of source. " \
                    "Whoever figures out the source must shout it out. " \
                    "Whoever shouts out first, if the player is correct, they will earn a point for their team. "\
                    "However, if the player is incorrect, their team will lose two points. Let me know when you "\
                    "are ready to continue onto the next question. Now, let the fun begin!"
    return playSound(speech_output)

def handle_session_end_request(string):
    # card_title = "Session Ended"
    # speech_output = string + "<break time='3s'/> Wow! That was really fun and intense! Thank you for playing with me today. " \
    #                 "I hope you all had fun! "
    return{
        'version': '1.0',
        'sessionAttributes': {},
        'response': { 
            'outputSpeech': {
                'type': 'SSML',
                'ssml':  "<speak>"+speech_output+"</speak>"   
                
            },
            'reprompt': { 
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': ""
                }
            },
            'shouldEndSession': True
        }
    }
    
def playSound(addString):
    shouldEnd = False
    return{
        'version': '1.0',
        'sessionAttributes': {},
        'response': { 
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>"+addString +"</speak>"         
                
            },
            'reprompt': { 
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': ""
                }
            },
            'shouldEndSession': shouldEnd
        }
    }
def nextGuess():

    temp = randint(0,14)
    audio=getMusic(temp*2)

    ans = getCat(temp*2 +1)
    os.environ['ans']=ans
    playSound(os.environ['ans'])
    return{
        'version': '1.0',
        'sessionAttributes': {},
        'response': { 
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak> "+audio+audio+"Was that an Animal, Human, machine, or other noise? </speak>"         
                
            },
            'reprompt': { 
                'outputSpeech': {
                    'type': 'SSML',
                'ssml': "<speak>"+audio+audio+"Again, Was that an Animal, Human, machine, or other noise? </speak>"   
                }
            },
            'shouldEndSession': False
        }
    }
    
def none():
    if('other' != os.environ['ans']):
        return wrong()
    else:
        return right()
    
def animal():
    if('animal'==os.environ['ans']):
        return right()
    else:
        return wrong()
    
def human():
    if('human'==os.environ['ans']):
        return right()
    else:
        return wrong()
    
def machine():
    if('machine'==os.environ['ans']):
        return right()
    else:
        return wrong()
        
def right():
    return playSound(getWinner(randint(0,4))+" Your team earned a point!")
    
def wrong():
    return playSound( getLower(randint(0,4))+" Your team lost two points...")
    
def noOneKnows():
    return nextGuess()
    
def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "saidNone":
        return none()    
    elif intent_name == "saidAnimal":
        return animal()
    elif intent_name == "saidHuman":
        return human()
    elif intent_name == "saidMachine":
        return machine()
    elif intent_name == "nextQuestion":
        return noOneKnows()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +", sessionId=" + session['sessionId'])

def lambda_handler(event, context):
    
    print("event.session.application.applicationId=" +event['session']['application']['applicationId'])
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])