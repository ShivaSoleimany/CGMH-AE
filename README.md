# General Chatbot
General Conversational Agent.

## How to install
```
git clone https://github.com/altaml/general_chatbot.git
cd general_chatbot
pip install -r requirements.txt
python setup.py install
```

## How to Run

### Duckling Docker
[Rasa Duckling Docker](https://hub.docker.com/r/rasa/duckling/) is used for entity extraction in the following dimensions:
- time
- number
- amount-of-money"
- distance
- duration
- email
- phone-number

Run `docker run -d -p 8000:8000 rasa/duckling`.

### Slackbot
```
python chatbot_core/slackbot/bot.py "NLU Model"
```
Currently available `"NLU Model"`s:
- v0.1

## Intents

- [x] Greeting
- [x] Good_Bye
- [x] Thank_You
- [x] Ask_Help
- [x] Ask_Fun
- [x] Ask_Marriage
- [x] Repeat
- [x] Ambiguous
- [x] Compliment
- [ ] Weather
- [ ] Time
- [ ] Affirm
- [ ] Search_Location

## Chatbot Architecture

```
              ______
               User
              ______
                ^  response
                |
                v  request
          ______________
            User Agent    ---> (Slack, FB, Website, ...)
          ______________
                ^ response
                |
                v request
          _______________
           Agent Manager
          _______________
 * intents    ^        ^ resopnse
 * entities /          \
           /            \
          /              \  * intents
         v request        v * entities
     ______________  _____________
          NLUs          Systems
     ______________  _____________

```


