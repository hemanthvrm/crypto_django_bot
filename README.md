# Django Telegram Bot 

## Introduction
Django bot 1.0.
Used traditional django webhook style to trigger the response based on dialogflow request.

(sample images at end of the document)

## Requirements:
Dialogflow account
Python 3.6
Django==1.11

(Make sure you use virtualenv)
## Setup:
 Clone the Repository

    > git clone https://github.com/hemanthvrm/crypto_django_bot
    > cd crypto_django_bot

**Install dependencies**

    pip3 install -r requirements.txt

**Run migrations**

    python manage.py migrate

**Start the local server**

    python manage.py runserver

**Download ngrok**
To generate public url for localhost for webhook testing purpose

    ngrok http 8000

It generates something like  http://5e9754f8.ngrok.io   (example)

## Dialogflow (Follow documentation for complete structure)
Create an account in dialogflow and enable telegram bot in integrations section.
(you can enable any bot ex:-slack/skype/fb/line)

**Go to  Fulfillment tab**

Enable webhook and paste the ngrok url which we generated earlier in the below format.

    http://5e9754f8.ngrok.io/cryptoprice/1234random/

**Got to intent tab**

Provide name for the intent, provide anything in usersays section and right click to add entity(select system.any). 
Provide action name as cryptoprice.
Enable webhook at the end of the page.



> 	Provide response at telegram resposne slot without enabling webhook
> at the bottom, For intents which dosen't need any action to be
> performed.
>  Ex: User Says:  Hi
>       Telegram response: Hello 
>       Or you can enable small talk for this this type of conversation with bot. 


Once everything was setup, your bot response will be as shown in this picture


I utilized coinmarketcap api to get the price details.
Similarly based on action name you can perform rest calls to different public api's


**Next update:**
Working on django channels instead of traditional approach.


**Sample images:**
*Dialogflow intent, Telegram web chat screenshot, Telegram mobile screenshot*

![Dialogflow intent page](https://github.com/hemanthvrm/Python/blob/master/df_intent_1.PNG)
![Telegram mobile chat](https://github.com/hemanthvrm/Python/blob/master/mobiletelegram.png)
![Telegram web chat](https://github.com/hemanthvrm/Python/blob/master/webtelegram.PNG)

 
