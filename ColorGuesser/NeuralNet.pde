public class NeuralNet {
  float[] bWeights = new float[3]; // 0 is r, 1 is g, 2 is b
  float[] wWeights = new float[3];
  float bConfidence;
  float wConfidence;
  
  NeuralNet() {
    for (int i = 0; i < bWeights.length; i++) {
      bWeights[i] = random(-1, 1);
      wWeights[i] = random(-1, 1);
    }
  }
  
  //---------------------------------------------------------
  
  void guess(int[] colors) {
    bConfidence = 0;
    wConfidence = 0;
    
    for (int i = 0; i < bWeights.length; i++) {
      bConfidence += bWeights[i] * colors[i];
      wConfidence += wWeights[i] * colors[i];
    }
    
    bConfidence = sigmoid(bConfidence);
    wConfidence = sigmoid(wConfidence);
  }
  
  float sigmoid(float num) {
    return 1 / (1 + pow(exp(1), -num));
  }
  
  void train(char choice) {
    float bActual = (choice == 'b')? 1: 0;
    float wActual = (choice == 'b')? 0: 1;
    float LEARNING_RATE = 0.01;
    float error = bActual - bConfidence;
    
  }
}
