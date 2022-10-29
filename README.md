# VerbGameBot

for auth
install gloud cli

https://googleapis.dev/python/google-api-core/latest/auth.html

run gcloud auth application-default login
if there any errors please see a suggestions
probably you need to add quota for your project
gcloud auth application-default set-quota-project <your_project_name>
copy .json to your python project directory
open .env and copy path to the .json like this:
GOOGLE_APPLICATION_CREDENTIALS=verbgamebot_credentials.json
GOOGLE_CLOUD_PROJECT=verbgamebot
