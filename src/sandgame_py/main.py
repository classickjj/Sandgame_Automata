import settings
import IOevents #THIS IMPORT IS VERY IMPORTANT! otherwise IOevents will not work while app is running!!! 
from board import run_board

################################################# MAIN ################################################

if __name__ == "__main__":
    #run game setup and start the game loop
    run_board()
    settings.root.mainloop()