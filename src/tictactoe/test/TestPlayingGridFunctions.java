package tictactoe.test;

import tictactoe.utils.*;

public class TestPlayingGridFunctions {

  public static void main(String[] args) {
    int playingGridSize = 3;
    PlayingGrid playingGrid = new PlayingGrid(playingGridSize);

    for (int i = 0; i < playingGridSize; i++) {
      for (int j = 0; j < playingGridSize; j++) {
        playingGrid.setValueAt(i, j, 'x');
      }
    }
    
    playingGrid.printPlayingGrid();
    System.out.println();
    playingGrid.printGridInfo();
  }
}
