import world
from player import Player

def play(map,game_level_int):
    world.load_tiles(map,game_level_int)
    player = Player()
    #These lines load the starting room and display the text
    x, y = world.starting_position
    room = world.tile_exists(x,y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    print("""
    Welcome to the Game, 
    You are going to enter a post-apolocalytpic world infested by Zombies, Draculas and 
    Werewolves.
    The First level starts in Hof City where the T-Virus has infected all of your friends and fellow-residents.
    The Second level starts in the City of Mannheim. This contains even stronger enemies.
    The Third level is a mix of creatures with creatures like Alpha-Werewolf, Dracula and a Dracula+Zombie hybrid
    lurking around.
    
    
          """)
    game_level= input('Please Select game Level: ')
    game_level_int=int(game_level)
    if game_level_int>3 and game_level_int<1:
        print('Restart the game with a valid Level')


    selected_map="map"+str(game_level_int)+".txt"
    play(selected_map,game_level_int)