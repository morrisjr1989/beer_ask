
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from beerlocation import QueryForBeer

app = Flask(__name__)

ask = Ask(app, "/open_brewery")

@app.route('/')
def homepage():
    return ''

@ask.launch
def start_skill():
    return question('Welcome to Beer Querry - What city and state are you looking for?')

@ask.intent('CityState')
def city_state(city, state):

    #TODO create dialog model to investigate data from LocationQuery

    breweries = QueryForBeer(city, state).LocationQuery()
    response  = 'For {}, {} I have found {} breweries'.format(city, state, len(breweries))

    return statement(response)



@ask.intent('AMAZON.FallbackIntent')
def fallback():
    to_continue = render_template('to_continue')
    return question('Sorry, I am not sure what you asked me...{}'.format(to_continue))


@ask.intent('AMAZON.NavigateHomeIntent')
def go_home():
    return question('et - phone home')


@ask.intent('AMAZON.HelpIntent')
def help_me():
    help_me_text = render_template('help')
    return question(help_me_text)


@ask.intent('Credits')
def speak_credits():
    credits_ = render_template('credits')
    return statement(credits_)


@ask.intent('AMAZON.StopIntent')
def stop():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)





