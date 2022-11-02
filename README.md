# VerbGameBot

The dialog blog integrated to Telegram and vk.vom.
The bot uses DialogFlow ES by Google for conversation.

### How to install

- Firstly create Google Cloud account;
- Then you have to create DialogFlow account;
and create a project there. For more information
go to the link https://cloud.google.com/dialogflow/es/docs/quick/setup
- Copy the project ID. It needs later for filling of
requested variable in .env;
- Create an agent "Intent" that uses for your 
conversation topics. For more information visit the following link:
https://cloud.google.com/dialogflow/docs/quick/build-agent
- For additional intents use script:

```
create_intent.py
```

- If you have kind of permission denied error
you have to authorize on google. Please install google-cli:

https://googleapis.dev/python/google-api-core/latest/auth.html

- Run: 

```
gcloud auth application-default login
```

- If there are any errors please see a suggestions.
Probably you need to add a quota for your project:

```
gcloud auth application-default set-quota-project <your_project_name>
```

- Copy .json to your python project directory -> `verbgamebot_credentials.json`
- Use .env.example as a draft and fill all of the requested
variables:

```
TELEGRAM_TOKEN='YOUR_TELEGRAM_TOKEN'
VK_TOKEN='VK_GROUP_TOKEN'
GOOGLE_APPLICATION_CREDENTIALS='JSON_WITH_GOOGLE_CREDENTIALS'
GOOGLE_CLOUD_PROJECT='ID_OF_GOOGLE_CLOUD_PROJECT'
```

### How to start

Run in a terminal:

```
tg_bot.py
vk_bot.py
```

### Deploy with Docker

1. Copy this repository to your server:
```
git clone git@github.com:Gennadynemchin/VerbGameBot.git
```
2. `cd VerbGameBot`
3. `nano .env.example`. Then fill all needed variables as shown above;
4. `nano verbgamebot_credentials.json.example` Then save it;
5. Save google credentials as `verbgamebot_credentials.json`
6. Build an image:
`docker build -t your-image-name . `
7. Then `docker run -d --restart always your-image-name`
