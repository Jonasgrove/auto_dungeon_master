#!/usr/bin/env python

from typing import List
import json

from auto_dungeon_master import utilities as utils
from auto_dungeon_master import constants
from auto_dungeon_master.player import DNDPlayer
from auto_dungeon_master.campaign import Campaign

class AutoDungeonMaster:
    """
    Class for encapsulating the dungeon master. This class is responsible for
    taking in the conext of the campaign, the player information, and conceiving
    the orchestrating the actions that take place in the session. 
    """
    def __init__(self,
                 campaign_db: str = None) -> None:
        self.campaign_name = ""
        self.campaign_desc = ""
        self.campaign_db = campaign_db
        self.num_players = 0
        self.players = dict()
        self.campaign = None
        self.turn = 0
        self.game_over = False
    
    def start_new_campaign(self):
        """
        Create a campaign by initializing the characters and sending an API request
        to the resquest with the campaign description and the character information.
        """
        self.respond(constants.LOGO)
        self.respond(constants.WELCOME_INTRO)
        self.campaign_name = input("Please enter a name for your campaign: ")
        self.campaign_desc = input("Please enter a brief description of the adventure you want to embark on: ")
        self.num_players = int(input("Please enter the number of adventurers you would like to have in your game: "))

        self.set_players()
        start_game_prompt = constants.NEW_GAME_SYSTEM_PROMPT.format(
            game_description=self.campaign_desc,
            player_information=self._get_all_player_info()
        )
        response = utils.make_api_request(
            context=start_game_prompt,
            prompt=constants.NEW_GAME_USER_PROMPT
        )

        self.campaign = Campaign(
            name=self.campaign_name,
            current_response=response,
            campaign_context={f"dm_turn_{self.turn}": response}
        )
        self.respond(response)

    def set_players(self):
        """
        Initialize the players in the game by prompting for each player to
        enter their desired attributes. After every player has entered their
        information, the DNDPlayer objects are put in a dictionary of character
        names pointing to their corresponding objects.
        """
        for player_i in range(self.num_players):
            player_obj = self._get_player(player_i)
            player_name = player_obj.player_name
            self.players[player_name] = player_obj
    
    def _get_player(self, player_num: int) -> DNDPlayer:
        """
        Prompt the user to get the information for a player and create a DNDPlayer
        object using the information.
        """
        player_name = utils.prompt_for_player_input(
            f"Welcome to the game adventurer {player_num}! Please enter your name: "
        )
        player_race = utils.prompt_for_player_input(
            f"Hello {player_name}! Please tell me your race: "
        )
        player_class = utils.prompt_for_player_input(
            f"Now please tell me your class, {player_name}: "
        )
        player_description = utils.prompt_for_player_input(
            f"Now, {player_name}, please tell me about yourself. " \
            f"Tell me about you previous life, ideals, physical characteristics, personality and alegience: "
        )
        player_level = constants.DFLT_PLAYER_LEVEL
        player_inventory = constants.DFLT_PLAYER_INVENTORY
        player_spells = constants.DFLT_PLAYER_SPELLS
        player_gold = constants.DFLT_PLAYER_GOLD

        player_obj = DNDPlayer(
            player_name=player_name,
            player_race=player_race,
            player_class=player_class,
            player_level=player_level,
            player_inventory=player_inventory,
            player_spells=player_spells,
            player_gold=player_gold,
            player_description=player_description,
        )

        return player_obj

    def _get_all_player_info(self) -> str:
        """
        Return a json formatted string of all the information about
        each player. 
        """
        all_player_info = {
            player_name: player_obj.get_player_info()
            for player_name, player_obj in self.players.items() 
        }
        all_player_info = json.dumps(all_player_info)

        return all_player_info

    def dungeon_master_turn(self):
        """
        Executes the turn of the dungeon master
        """
        print("dm turn")
    
    def players_turn(self):
        """
        Execute the turn of a player
        """
        print("player turn")

    def respond(self, msg):
        """
        Placeholder method for communicating information via the CLI.
        TODO add formatting
        """
        print(msg)
    