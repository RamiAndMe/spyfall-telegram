### Libraries ###
# Mini Telegram Bot Library
from tbot import TBot

# Reading CSV
import pandas as pd

# Self Explanatory
import time
import random
from pprint import pprint

### Setup ###
# Create Bot
bot = TBot(<Insert your bot token here>)
bot.get_updates() # Clear Updates

# Read CSV
location_roles_csv = pd.read_csv('Spyfall_LocationRoles.csv').loc[:, 'Airplane':'Passenger Train']
location_roles = {location: location_roles_csv[location].dropna().tolist() for location in location_roles_csv.columns}

game_rooms = {}
player_names = {}   # player_id: player_name

# What's inside location_roles?
# Location Roles stores location and the roles available for that locatin
# location_roles =
# {<location1>: [role1, role2, role3, ...],
#  <location2>: [role8, role9, role10, ...]}
#
# Sample Output
# {'Airplane': ['First Class Passenger',
#               'Air Marshall',
#               'Mechanic',
#               'Economy Class Passenger',
#               'Stewardess',
#               'Co-Pilot',
#               'Captain'],
#  'Bank': ['Armored Car Driver',
#           'Manager',
#           'Consultant',
#           'Customer',
#           'Robber',
#           'Security Guard',
#           'Teller']}

# What to store inside game_rooms?
# game_rooms =
# {<room-id>: {
#   'players':  [<list of user-id>],
#   'roles':    [<list of roles corresponding to user>],
#   'location': <location>,
#   'duration': <duration>
#   'end':      <end timing>
# }}
#
# Sample Output
# {781520638: {'end': 1556865023.722711,
#              'duration': 10
#              'location': 'Airplane',
#              'players': [781520638, ...],
#              'roles': ['Spy', ...]}}

# A user wants to create a game
def create_new_game(user_id, duration):
    # Use the user_id as the room_id


    # Create en 'empty' game_room
    # with only the user
    # rmr that duration is in secs! duration given is in mins


    # Remember to tell the user what's the room_id
    # so his/her friends can join!


# A user enters the room_id and wants to join the game
def join_game(user_id, room_id):
    # What if the room does not exist?
    # We need to tell the user and stop the code now


    # Find the Game Room / Create variable called 'game_room'


    # Create variable called 'players'
    # to capture players of the game


    # Add the user into the game
    # But what if the user is already in the game?


    # Tell the user that he/she has been added!


# Game Leader wants to start the game
def start_game(user_id):
    # Remember that room_id == user_id
    # Create variable "room_id"


    # What if the room does not exist?


    # Create variable "game_room"


    # Randomly choose
    # Store variable as "location"


    # Get the roles of that location
    # Store variable as "roles"


    # One person will be the spy so
    # how many non-spies role will there be?
    # Sample and Store as variable "player_roles"
    # Create "players" variable first


    # Add Spy into "player_roles"


    # So the last person will always be a spy?
    # Randomise by shuffling players


    # Store the variables (player, roles and location) into game_room


    # Still remember that there is a time limit?
    # Update game_room['end']
    # Use time.time() to get the time now (in seconds)


    # Message the players of that room
    # that the game has started.
    # Don't fret if the following code is long
    # Feel free personalise your messages


# When the game duration ends
def check_timeout():
    # Loop through each game room
        # And check if game ending time is less than the time now
        # Cus that means that the ending time has arrived
    # Tell the players that their time is up


    # Some questions to ponder:
    # 1. But wait, have you check what's the initial value of the ending time?
    # 2.
    # This function is going to be called every 5 seconds
    # What if we didn't extend the ending_time when the game timeout?
    # The users will get SPAMMED WITH MESSAGES!
    # Check that you have extended the ending time
    # So that the players will have time to vote (5 mins preferable?)

# User wants to end the game and reveal the results
def end_game(user_id):
    # Remember room_id == user_id

    # Validate parameters as always
    # Check room exists else stop code


    # Reveal the secrets!
    # Tell whose the spy
    # I'll let you figure the code for this one!
    # Collate the roles and send to all players


    # How to find player name?
    # Clue: Global Variable - 'player_names'
    # It consists of:
    # <player_id>: <player_name>

    # Btw, reminder to delete the game room afterwards.

# Done for you
# Function to check for newcomer and add their name to 'player_names'
# as well as to INTRODUCE THE GAME TO THEM WOOOOO
def check_newcomer(user_id):
    if chat_id not in player_names:
        user_name = message['chat']['first_name']
        player_names[chat_id] = user_name
        bot.send_message(chat_id,
        'Hello! Welcome to SpyFall!\n'
        'Type: "/newgame <Duration (mins)>" to create a new game\n'
        'Type: "/join <Room ID>" to join an existing game\n'
        'Type: "/start" to start an existing game (For team leaders)\n'
        'Type: "/end" to end an existing game (For team leaders)')


start_time = time.time()
while True:
    # Refreshes every 5 seconds
    time.sleep(max(0, start_time + 5 - time.time()))
    start_time = time.time()

    # Checks Game Timeout
    check_timeout()

    # Get Updates
    updates = bot.get_updates()

    # Loop Through each update
    for update in updates:
        # Checks if it's a message because
        # Telegram supports others like 'edited messages', 'poll', etc...
        if update.get('message'):
            message = update['message']
            text = message['text']
            parse = text.split() # String: '/newgame 10' --> List: ['/newgame', '10']
            chat_id = message['chat']['id']

            # Check for Newcomers
            check_newcomer(chat_id)

            if parse[0] == '/newgame':
                # Validation
                error = None
                if len(parse) < 2:
                    error = 'Error: Did you forget to specify duration?'
                elif not parse[1].isdigit():
                    error = 'Duration must be an integer'

                if error:
                    bot.send_message(chat_id, error)
                    continue

                duration = int(parse[1])
                create_new_game(chat_id, duration)

            elif parse[0] == '/join':
                room_id = parse[1]
                join_game(chat_id, room_id)

            elif parse[0] == '/start':
                start_game(chat_id)

            elif parse[0] == '/end':
                end_game(chat_id)

        pprint(game_rooms)