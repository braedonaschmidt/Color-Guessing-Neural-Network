ColorCircle b;
ColorCircle w;
NeuralNet net;

void setup() {
  size(800, 800);
  
  b = new ColorCircle(width / 4, height / 2, "Black", 0);
  w = new ColorCircle(width / 4 * 3, height / 2, "White", 255);
  
  net = new NeuralNet();
}

void draw() {
  int[] colors = {0, 255, 255};
  b.drawCircle(colors);
  w.drawCircle(colors);
  net.guess(colors);
  
  //println(net.bConfidence, net.wConfidence);
}

void mouseClicked() {
  if (b.inCircleBounds(mouseX, mouseY)) print("b");
  if (w.inCircleBounds(mouseX, mouseY)) print("w");
}

//void
