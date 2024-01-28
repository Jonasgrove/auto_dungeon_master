# Auto Dungeon Master (AutoDM)

## A repository for a AI enabled dungeon master for playing DND

**Repo Layout**
```
auto_dungeon_master
    |_campaign.py            # class that maintains the history of the campaign that is ongoing
    |_auto_dm.py             # class to maintain the dm for the campaign, this is the AI that is communicated knowledge to
    |_player.py              # class to store information about the player, including race, class, stats and items
    |_utilities.py           # utility functions for game operations
    |_constants.py           # constants for consistant values
campaign_database
    |_campaign_database.sql  # sqlite database that contains the game information
    |_orm
        |_models.py          # sqlalchemy models
        |_engine.py          # sqlalchemy engine
        |_session.py         # sqlalchemy session
```