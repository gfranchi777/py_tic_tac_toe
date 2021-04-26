package tictactoe.utils;

/**
 *
 * @author wpnx777
 */
public class GridPosition {

  private int x;
  private int y;
  private char value;

  /**
   *
   */
  public GridPosition() {

  }

  /**
   *
   * @param x
   * @param y
   * @param value
   */
  public GridPosition(int x, int y, char value) {
    setX(x);
    setY(y);
    setValue(value);
  }

  /**
   *
   * @param x
   */
  public void setX(int x) {
    this.x = x;
  }

  /**
   *
   * @param y
   */
  public void setY(int y) {
    this.y = y;
  }

  /**
   *
   * @param value
   */
  public void setValue(char value) {
    this.value = value;
  }

  public void setPosition(int x, int y, char value) {
    setX(x);
    setY(y);
    setValue(value);
  }
  
  /**
   *
   * @return
   */
  public int getX() {
    return this.x;
  }

  /**
   *
   * @return
   */
  public int getY() {
    return this.y;
  }

  /**
   *
   * @return
   */
  public char getValue() {
    return this.value;
  }
}
