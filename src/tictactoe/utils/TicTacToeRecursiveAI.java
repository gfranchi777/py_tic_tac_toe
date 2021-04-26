/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tictactoe.utils;

/**
 *
 * @author wpnx777
 */
public class TicTacToeRecursiveAI {

  public TicTacToeRecursiveAI() {

  }

  public GridPosition makeMove(int x, int y) {
    GridPosition gridPosition = new GridPosition();

    if (x == PlayingGrid.PLAYING_GRID_WIDTH
            && y == PlayingGrid.PLAYING_GRID_HEIGHT) {
      gridPosition.setPosition(9, 9, 'X');
    }

    return gridPosition;
  }
}
