package tictactoe.utils;

/**
 *
 * @author giancarlo.franchi
 *
 */
public class TicTacToeAI {

  /**
   * Class Variables
   */
  //Variable used to determine if a new game has begun.
  private boolean isFirstMove;
  //Variable used to determine if the AI has made a move.
  private boolean moveMade;

  /**
   * Default Constructor
   */
  public TicTacToeAI() {
    setIsFirstMove(true);
    setMoveMade(false);
  }//End Method TicTacToeAI

  /**
   *
   * @param isFirstMove
   */
  public void setIsFirstMove(boolean isFirstMove) {
    this.isFirstMove = isFirstMove;
  }//End Method setIsFirstMove

  /**
   *
   * @param moveMade
   */
  public void setMoveMade(boolean moveMade) {
    this.moveMade = moveMade;
  }//End Method setMoveMade

  /**
   *
   * @param grid
   * @param row
   * @param col
   * @param value
   */
  public void makeMove(PlayingGrid grid, int row, int col, char value) {
    grid.setValueAt(row, col, value);
  }//End Method makeMove

  /**
   *
   * @return
   */
  public boolean isFirstMove() {
    return isFirstMove;
  }//End Method isFirstMove

  /**
   *
   * @param grid
   * @return
   */
  public boolean winPossible(PlayingGrid grid) {
    boolean winPossible = false;

    return winPossible;
  }//End Method winPossible

  /**
   *
   * @param grid
   * @return
   */
  public boolean blockRequired(PlayingGrid grid) {
    boolean blockRequired = false;

    return blockRequired;
  }//End Method blockRequired

  /**
   *
   * @param grid
   * @return
   */
  public boolean makeCenterMove(PlayingGrid grid) {
    grid.setValueAt((grid.size() - 1) / 2, (grid.size() - 1) / 2, 'X');
    setMoveMade(true);

    return moveMade;
  }//End Method makeCenterMove

  /**
   *
   * @param grid
   * @return
   */
  public boolean makeCornerMove(PlayingGrid grid) {
    for (int i = 0; i < grid.getGridCorners().size(); i++) {
      if (grid.getGridCorners().get(i).getValue() == ' ') {
        makeMove(grid, grid.getGridCorners().get(i).getX(),
                grid.getGridCorners().get(i).getY(), 'X');
        setMoveMade(true);
        break;
      }
    }
    return moveMade;
  }//End Method makeCornerMove

  /**
   *
   * @param grid
   * @return
   */
  public boolean makeSideMove(PlayingGrid grid) {
    for (int i = 0; i < grid.getGridSides().size(); i++) {

    }

    return moveMade;
  }//End Method makeSideMove

  /**
   *
   * @param grid
   * @return
   */
  public boolean eval(PlayingGrid grid) {
    setMoveMade(false);
    //Check if the first move has been made yet.
    if (grid.valueAt((grid.size() - 1) / 2, (grid.size() - 1) / 2) == 0) {
      makeCenterMove(grid);
    } else {
      //Check if AI win is possible.
      if (!winPossible(grid)) {
        //If needed, block human from winning.
        if (!blockRequired(grid)) {
          //No win possible, no block required, make random move.
          if (!makeCornerMove(grid)) {
            makeSideMove(grid);
          }//End if
        }//End if
      }//End if
    }//End if
    return moveMade;
  }//End eval()
}//End Class TicTacToeAI
