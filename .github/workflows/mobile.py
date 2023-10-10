import pandas as pd

class DataAnalyzer:

  def __init__(self, train_file, test_file): 
    self.train_file = train_file
    self.test_file = test_file
    self.train_data = None
    self.test_data = None

  def load_data(self):
    # Load training data
    self.train_data = pd.read_csv(self.train_file)
    
    # Load test data
    self.test_data = pd.read_csv(self.test_file)

  def summarize_data(self):
    print("Summary of training data:")
    print(self.train_data.describe())
    
    print("Summary of test data:") 
    print(self.test_data.describe())

if __name__ == "__main__":

  analyzer = DataAnalyzer("train.csv", "test.csv")
  analyzer.load_data()
  analyzer.summarize_data()
