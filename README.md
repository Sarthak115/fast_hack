Weather Forecasting CLI Tool
Weather Forecast CLI Tool is a Python based application that allows users to fetch the current weather information for any city using Open WeatherMap's API. Users can provide the city name via the command line, and the tool retrives the weather information for the specified city

Features
Fetch current weather information for any city Simple and intitutive command-line interface Relies on OpenWeatherMap's API for data retrieval

Pre-reqisities
Python 3.x

API key from OpenWeatherMap

Installation - How to use this code ?
Clone this repository or download the source code

git clone https://github.com/Fastest-Coder-First/fastesthack-python-rv.git

cd fastesthack-python-rv
Install dependencies

pip install requests

Set the OpenWeatherMap API Key as an environment variable.

On windows:

Set environment variable "api_key" with your key using below steps:

a. Right-click on the computer icon on your desktop or in File explorer, and then select properties

b. Click on Advanced system settings on the left panel

c. In the System Properties window, go to the Advanced tab and click the Environment variables button.

d. Under User variables or System variables, click New

e. Enter the variable name (eg. api_key) and value (eg. 'your_api_key') and then click OK.

f. Click OK to close the Environment Variables dialog and the System Properties dialog

After setting an environment variable through the Environment Variables dialog, you will need to restart any open Command 















This above diagram illustrates the interaction between different components in a high-level view:

User's Terminal: This is where the user interacts with the command-line tool. The user inputs the city name and the terminal displayes the weather forecast

Python Script: This Script is the core of the application. It fetches the API key from environment variables, takes city name as input, makes an HTTP request to OpenWeatherMap API, processes the data received, and finally displays the output in the terminal

OpenWeatherMap API: This is a third-party web service that processes the HTTP request made by the Python script and returns the weather data in response




USAGE:
Run the "fast.py" script and provide the name of the city as input when prompted.
Example input: Enter city name: DELHI

Sample output received during hackathon:














