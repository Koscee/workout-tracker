## Install Dependencies
```shell script
pip install requests
```
## Run Application
- Make sure you provide the following credentials as environment variables before running the application
```commandline
NIX_APP_ID
NIX_API_KEY
SHEETY_TOKEN
SHEETY_ENDPOINT
```
 - Generate ``NIX_APP_ID and NIX_API_KEY`` from [Nutritionix API](https://www.nutritionix.com/business/api)
 - Create a sheet in your google sheet with the following columns
 1. Date
 2. Time
 3. Exercise
 4. Duration
 5. Calories
 - Connect your google account with [Sheety](https://sheety.co/), create a new project "Workout Tracking"
 - Enable `POST` endpoint, copy the url and set is as ``SHEETY_ENDPOINT``
 - In the Sheety dashboard, click on "Authentication" and add a Bearer (Token).
 Copy the token and set it as ``SHEETY_TOKEN``
 - Run ``main.py``