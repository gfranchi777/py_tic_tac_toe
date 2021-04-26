package tictactoe.utils;

import java.util.*;

/**
 *
 * @author giancarlo.franchi
 *
 */
public class PlayingGrid {
  //Class Constants
  public static int PLAYING_GRID_WIDTH = 3;
  public static int PLAYING_GRID_HEIGHT = 3;
  
  //
  private int gridSize;
  private char[][] playingGrid;
  private ArrayList<GridPosition> gridCorners = new ArrayList<GridPosition>();
  private ArrayList<GridPosition> gridSides = new ArrayList<GridPosition>();

  /**
   *
   */
  public PlayingGrid() {
  }

  /**
   *
   * @param playingGridSize
   */
  public PlayingGrid(int playingGridSize) {
    setSize(playingGridSize);
    setPlayingGrid(playingGridSize);
    setCorners(playingGrid);
    setSides();
  }

  /**
   *
   * @param gridSize
   */
  public void setSize(int gridSize) {
    this.gridSize = gridSize;
  }

  /**
   *
   * @param playingGridSize
   */
  public void setPlayingGrid(int playingGridSize) {
    this.playingGrid = new char[playingGridSize][playingGridSize];
  }

  /**
   *
   * @param row
   * @param col
   * @param value
   */
  public void setValueAt(int row, int col, char value) {
    playingGrid[row][col] = value;
  }

  /**
   *
   * @return
   */
  public int size() {
    return gridSize;
  }

  /**
   *
   * @return
   */
  public char[][] getPlayingGrid() {
    return playingGrid;
  }

  /**
   *
   * @return
   */
  public ArrayList<GridPosition> getGridCorners() {
    return gridCorners;
  }

  /**
   *
   * @return
   */
  public ArrayList<GridPosition> getGridSides() {
    return gridSides;
  }

  /**
   *
   * @param row
   * @param col
   * @return
   */
  public char valueAt(int row, int col) {
    return playingGrid[row][col];
  }

  /**
   *
   * @param row
   * @param col
   * @return
   */
  public boolean isTaken(int row, int col) {
    boolean isTaken = false;

    if (valueAt(row, col) == 0) {
      isTaken = true;
    }

    return isTaken;
  }

  /**
   *
   * @param playingGrid
   */
  public void setCorners(char[][] playingGrid) {
    gridCorners.add(new GridPosition(0, 0, ' '));
    gridCorners.add(new GridPosition(0, gridSize - 1, ' '));
    gridCorners.add(new GridPosition(gridSize - 1, 0, ' '));
    gridCorners.add(new GridPosition(gridSize - 1, gridSize - 1, ' '));
  }

  /**
   *
   * @param playingGrid
   */
  public void setSides() {
    GridPosition tmpPosition = new GridPosition();
    tmpPosition.setValue(' ');

    for (int i = 0; i < gridSize; i++) {
      tmpPosition.setX(i);
      for (int j = 0; j < gridSize; j++) {
        tmpPosition.setY(j);

        if (!isCenterPosition(tmpPosition)) {
          if (!isCornerPosition(tmpPosition)) {
            gridSides.add(new GridPosition(i, j, ' '));
          }
        }
      }
    }
  }

  /**
   *
   * @param gridPosition
   * @return
   */
  public boolean isCornerPosition(GridPosition gridPosition) {
    boolean isCorner = false;

    for (int i = 0; i < gridCorners.size(); i++) {
      if (gridPosition.getX() == gridCorners.get(i).getX()
              && gridPosition.getY() == gridCorners.get(i).getY()) {
        isCorner = true;
      }
    }
    return isCorner;
  }

  /**
   *
   * @param gridPosition
   * @return
   */
  public boolean isCenterPosition(GridPosition gridPosition) {
    boolean isCenter = false;

    if (gridPosition.getX() == (gridSize - 1) / 2
            && gridPosition.getY() == (gridSize - 1) / 2) {
      isCenter = true;
    }
    return isCenter;
  }

  /**
   *
   */
  public void printPlayingGrid() {
    for (int i = 0; i < gridSize; i++) {
      for (int j = 0; j < gridSize; j++) {
        if (j < gridSize - 1) {
          System.out.print(playingGrid[i][j] + "|");
        } else {
          System.out.print(playingGrid[i][j]);
        }
      }
      System.out.println();
    }
  }

  /**
   *
   */
  public void printGridInfo() {
    System.out.println("Center Position Info:");
    System.out.println("X: " + (gridSize - 1) / 2);
    System.out.println("Y: " + (gridSize - 1) / 2);
    System.out.println();

    System.out.println("Corner Positions Info:");
    for (int i = 0; i < gridCorners.size(); i++) {
      System.out.println("X: " + gridCorners.get(i).getX());
      System.out.println("Y: " + gridCorners.get(i).getY());
      System.out.println();
    }

    System.out.println("Side Positions Info:");
    for (int i = 0; i < gridSides.size(); i++) {
      System.out.println("X: " + gridSides.get(i).getX());
      System.out.println("Y: " + gridSides.get(i).getY());
      System.out.println();
    }
  }
}
