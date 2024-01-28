#!/usr/bin/env python

# Game start prompts
LOGO = r"""

   ,---.                   ,--.--------.   _,.---._                                       
 .--.'  \     .--.-. .-.-./==/,  -   , -\,-.' , -  `.                                     
 \==\-/\ \   /==/ -|/=/  |\==\.-.  - ,-./==/_,  ,  - \                                    
 /==/-|_\ |  |==| ,||=| -| `--`\==\- \ |==|   .=.     |                                   
 \==\,   - \ |==|- | =/  |      \==\_ \|==|_ : ;=:  - |                                   
 /==/ -   ,| |==|,  \/ - |      |==|- ||==| , '='     |                                   
/==/-  /\ - \|==|-   ,   /      |==|, | \==\ -    ,_ /                                    
\==\ _.\=\.-'/==/ , _  .'       /==/ -/  '.='. -   .'                                     
 `--`        `--`..---'         `--`--`    `--`--''                                       
                          .-._            _,---.      ,----.     _,.---._    .-._         
  _,..---._  .--.-. .-.-./==/ \  .-._ _.='.'-,  \  ,-.--` , \  ,-.' , -  `. /==/ \  .-._  
/==/,   -  \/==/ -|/=/  ||==|, \/ /, /==.'-     / |==|-  _.-` /==/_,  ,  - \|==|, \/ /, / 
|==|   _   _\==| ,||=| -||==|-  \|  /==/ -   .-'  |==|   `.-.|==|   .=.     |==|-  \|  |  
|==|  .=.   |==|- | =/  ||==| ,  | -|==|_   /_,-./==/_ ,    /|==|_ : ;=:  - |==| ,  | -|  
|==|,|   | -|==|,  \/ - ||==| -   _ |==|  , \_.' )==|    .-' |==| , '='     |==| -   _ |  
|==|  '='   /==|-   ,   /|==|  /\ , \==\-  ,    (|==|_  ,`-._ \==\ -    ,_ /|==|  /\ , |  
|==|-,   _`//==/ , _  .' /==/, | |- |/==/ _  ,  //==/ ,     /  '.='. -   .' /==/, | |- |  
`-.`.____.' `--`..---'   `--`./  `--``--`------' `--`-----``     `--`--''   `--`./  `--`  
         ___    ,---.        ,-,--.  ,--.--------.    ,----.                              
  .-._ .'=.'\ .--.'  \     ,-.'-  _\/==/,  -   , -\,-.--` , \  .-.,.---.                  
 /==/ \|==|  |\==\-/\ \   /==/_ ,_.'\==\.-.  - ,-./==|-  _.-` /==/  `   \                 
 |==|,|  / - |/==/-|_\ |  \==\  \    `--`\==\- \  |==|   `.-.|==|-, .=., |                
 |==|  \/  , |\==\,   - \  \==\ -\        \==\_ \/==/_ ,    /|==|   '='  /                
 |==|- ,   _ |/==/ -   ,|  _\==\ ,\       |==|- ||==|    .-' |==|- ,   .'                 
 |==| _ /\   /==/-  /\ - \/==/\/ _ |      |==|, ||==|_  ,`-._|==|_  . ,'.                 
 /==/  / / , |==\ _.\=\.-'\==\ - , /      /==/ -//==/ ,     //==/  /\ ,  )                
 `--`./  `--` `--`         `--`---'       `--`--``--`-----`` `--`-`--`--'
               """

WELCOME_INTRO = "A Role Playing Game (poorly) powered by Artifical Inteligence. \n" \
                "To begin the game, you will need to enter the name of your campaign, \n" \
                "a brief description of the world you want to explore, and the number \n" \
                "of players that will be participating. After this initial information is entered, \n" \
                "each player will be prompted to enter their initial character information."


# API request templates
NEW_GAME_SYSTEM_PROMPT = "You are a dungeon master for the RPG dungeons and dragons. " \
                         "Your job is to design and coordinate a DND campaign based on this description: {game_description} " \
                         "The players in the campaign will invlove these characters provided in json format: {player_information}"

NEW_GAME_USER_PROMPT = "Please initialize the dungeons and dragons campaign and provide an initial set of actionable options for the characters to embark on."

EXISTING_GAME_SYSTEM_PROMPT = "You are a dungeon master for the RPG dungeons and dragons. " \
                              "You are coordinating the campaign that is described here: {game_context}. " \
                              "The players participating in the campaign are described here: {player_information}."

EXISTING_GAME_USER_PROMPT = "Given the previous context provided about the campaign and the information about the players, " \
                            "provide a new set of actionable options for the characters to embark on."


DFLT_PLAYER_INVENTORY = {}
DFLT_PLAYER_LEVEL = 1
DFLT_PLAYER_GOLD = 1
DFLT_PLAYER_SPELLS = {}