import settings
import board



def water_rules(x, y):
    # Check if the current cell contains water and the cell below is empty
    if y + 1 < settings.cells_number_h:
        if settings.current_game_board[x][y + 1].get_type() == "Air":
            
            #print("\t>>found >>" + settings.current_game_board[x][y+1].get_type() + "<< under water at x: " + str(x) + " , y: " + str(y+1))
            # Move water downward
            settings.nextGen_game_board[x][y + 1].set_type("Water")
            settings.nextGen_game_board[x][y].set_type("Air")
            #print("\t>>switched water and air")
            # Update the changed cells
            settings.changed_cells.append((x, y + 1))
            settings.changed_cells.append((x, y))
            #print("\t>>added to changed cells")

        board.update_generations()
        #print("\t>>GRID UPDATED!!!")
        board.draw_game_board(settings.canvas, settings.current_game_board, settings.cell_width, settings.cell_height)
        #print("\t>>DRAWING DONE!!!")
            
def stone_rules(x, y):
    settings.nextGen_game_board[x][y].set_type("Stone")


