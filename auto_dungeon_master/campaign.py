#!/usr/bin/env python

import json
from dataclasses import dataclass


@dataclass
class Campaign:
    """
    Dataclass for storing the ongoing context of the campaign.
    Attributes:
        name (str): name of the campaign
        campaign_context (list): list of campaign context. The list
            consists of dictionaries of interctions formatted as
            [{"dm_turn_n": "turn_context"}, {"players_turn_n": "turn_context"}]

        
    """
    name: str
    current_response: str
    campaign_context: list

    def add_campaign_context(self, new_context: dict) -> None:
        """
        Add a new context entry to the campaign_context
        """
        self.campaign_context.append(new_context)

    def get_campaign_context(self):
        """
        Get a json formatted string of all of the campaign context
        up to this point.
        """
        json_campaign_context = json.dumps(self.campaign_context)

        return json_campaign_context


    




    

        