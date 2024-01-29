#!/usr/bin/env python

import argparse

from auto_dungeon_master.auto_dm import AutoDungeonMaster
 

def parse_arguments():
    parser = argparse.ArgumentParser(description='Start or Resume a Dungeons and Dragons Campaign.')

    parser.add_argument('--campaign_db',
                        required=False,
                        default=None,
                        type=str,
                        help='Path to existing DND Campaign database')

    args = parser.parse_args()

    return args



def main():
    args = parse_arguments()
    campaign_db = args.campaign_db

    if campaign_db:
        # TODO
        print("Loading campaign from database")

    game_over = False
    start_of_campaign = True
    game_in_session = True
    while not game_over:
        if start_of_campaign:
            auto_dm_obj = AutoDungeonMaster()
            auto_dm_obj.start_new_campaign()
            start_of_campaign = False
            auto_dm_obj.turn += 1

        elif game_in_session:
            auto_dm_obj.players_turn()
            auto_dm_obj.dungeon_master_turn()
            game_over = auto_dm_obj.game_over
            auto_dm_obj.turn += 1
            
        

            



if __name__ == "__main__":
    main()
