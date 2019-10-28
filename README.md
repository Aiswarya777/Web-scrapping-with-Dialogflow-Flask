# Web-scrapping-with-Dialogflow-Flask
To create a chatbot that scrapes data from the jobsite Indeed.com 

AIM
To create a chatbot that scrapes data from the jobsite Indeed.com (https://www.indeed.co.in/).

REQUIREMENTS
Python (version 3.7)
Dialogflow
Ngork

IMPLEMENTATION

1.	Install all required packages in python mentioned in requirements.txt
2.	Scrapping is done in the main file with beautifulsoup
3.	Install ngrok
4.	Create a Dialogflow Agent (https://dialogflow.com/#)
5.	In Dialogflow console under Settings ⚙ > Restore from Zip using the My_BOT.zip.
6.	Go to all intents and enable webhook
7.	Run the python files.
8.	This will run the program in default link https 5000
9.	Open ngrok , run command ngrok.exe http 5000
10.	Copy the link obtained(e.g. https://e06f01d9.ngrok.io)
11.	Paste the link in: Dialogflow--Fullfillment--Webhook--Enable switch--paste URL
12.	This is done to enable a webhook with our chatbot. Each session will be live for 8 hours.
13.	 Chat with the bot in the “try now” section and get the results.

ISSUES FACED:

Dialogflow webhooks need to response within 5 seconds or Dialogflow considers the fulfillment to have timed out and the response defined in Dialogflow’ s console will be surfaced (if present).
If the scrapping takes time more than 5 seconds, then the session will time out and webhook call fails.





