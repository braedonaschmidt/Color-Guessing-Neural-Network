public class ColorCircle {
  PVector loc;
  String word;
  int shade;
  int diameter = width / 3;
  
  ColorCircle(int x, int y, String word, int shade) {
    loc = new PVector(x, y);
    this.word = word;
    this.shade = shade;
  }
  
  //--------------------------------------------
  
  void drawCircle(int[] colors) {
    fill(colors[0], colors[1], colors[2]);
    circle(loc.x, loc.y, diameter);
    
    fill(shade);
    textAlign(CENTER, CENTER);
    textSize(height / 15);
    text(word, loc.x, loc.y);
  }
  
  boolean inCircleBounds(int x, int y) {
    return dist(x, y, loc.x, loc.y) <= diameter / 2;
  }
}
