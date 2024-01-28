#!/usr/bin/env python

import random

class DNDPlayer:
    """
    DNDPlayer class encapuslates the characteristics of a DND player
    and the logic for the simple actions that a player performs in the dnd game.
    """
    def __init__(self,
                 player_name: str,
                 player_race: str,
                 player_class: str,
                 player_level: int,
                 player_inventory: dict,
                 player_spells: dict,
                 player_gold: int,
                 player_description: str) -> None:
        self.player_name = player_name
        self.player_race = player_race
        self.player_class = player_class
        self.player_level = player_level
        self.player_inventory = player_inventory
        self.player_spells = player_spells
        self.player_gold = player_gold
        self.player_description = player_description
    
    def roll_dice(self, num_sides: int) -> int:
        """
        Simulate rolling a num_sides die and return the result.
        """
        if num_sides > 20 or num_sides < 1:
            raise ValueError(f"Invalid num_sides {num_sides} passed to 'roll_dice'")
        roll = random.randinit(1, num_sides)

        return roll

    def get_player_info(self):
        """
        Return a dictionary of the player information.
        """
        player_info = {
            "player_name": self.player_name,
            "player_race": self.player_race,
            "player_class": self.player_class,
            "player_level": self.player_level,
            "player_inventory": self.player_inventory,
            "player_spells": self.player_spells,
            "player_gold": self.player_gold,
            "player_description": self.player_description
        }

        return player_info

    






