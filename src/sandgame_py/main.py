import settings
import IOevents #THIS IMPORT IS VERY IMPORTANT! otherwise IOevents will not work while app is running!!! 
import board

################################################# MAIN ################################################

if __name__ == "__main__":
    #run game setup and start the game loop
    board.run_board()
    board.update_board()
    settings.root.mainloop()
    # Start the game loop by scheduling check_game_status and update_board functions
