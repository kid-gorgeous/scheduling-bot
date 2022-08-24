## School Reminder and Calender Application

This application will allow me(the user) to manage a database of reminders, and daily activities. It will allow Me(the user) to automatically receive chat reminders nearing a scheduled event


## The application at a glace

I would like this application to encompass a lot of things, but primarily I would like it to simplify and stream line my days. I would enjoy refreshing and timely reminders as to when my day is to begin and end, and ultimately how I'm going to be going from activity to activity at School, Employment, and my Free time.

## The big take away

This will help me plan, and execute my day. I will be able to rely on accurate time management. I can allow it to run in the background of my system, and allow it to actively check on me.

### Deeper connections and fun snippets

This application does not yet allow the user to received SMS messages,
but yet utilizes a popular messaging system Telegram. Not only will I(the user) received reminders over telegram, I will also receive them over Discord

### Setup

Setting up this Application is relatively easy. Since this project is in it's early infancy, I've opted to import a user made config file. Please create a new file in the host directory called 'config.py'. Gather your discord, and telegram api and assign them variable names. Make sure to import them to each time you open a new connection to the bot. 

####

#### This application is free and opeen sourse, if you would like to use it and improve it please post a pull request!

***
## Currently updating daily! 

#### Adding SQL Database, Scheduler, Alarm & Reminder System, and Chatbot Functionalities

### Creating a config file 

There are specific functions that are used thoughtout the application. In order to allow for the application to run properly please include the following lambda function, after import the os: clear = lambda: os.system('clear'). Next please create two user variables(user, and role). Set the user to your information, and the role to admin if you are using this for yourself. Finally, please create two string variables that will be initilized with a discord token and a telegram token (discord_token, telegram_token)