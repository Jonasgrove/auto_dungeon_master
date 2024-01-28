#!/usr/bin/env python

from dataclasses import dataclass


@dataclass
class Campaign:
    """
    Dataclass for storing the ongoing context of the campaign.
    Attributes:
        name (str): name of the campaign
        campaign_context (dict): dictionary of class context stored as
        
    """
    name: str
    current_response: str
    campaign_context: dict




    

        