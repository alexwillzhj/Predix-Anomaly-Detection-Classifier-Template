import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from analytics import tsAnomalyDetection

class test_anomaly_detection(unittest.TestCase):

    def test_anomaly_detection_with_file(self):

        analytic = tsAnomalyDetection()
        model_string = 1

        # map model
        modelmap = {"model_forecasting": model_string}

        # test with some data
        with open('./data/inputData/analytic_input_train.json') as json_input:
            print("Anomaly Detection: Classifier Training")
            analytic.ts_training(json_input.read(), modelmap)

        with open('./data/inputData/analytic_input_test.json') as json_input:
            print("Anomaly Detection: Classifier Testing")
            actual_output_data = analytic.ts_detection(json_input.read(), modelmap)

        print(actual_output_data)

if __name__ == "__main__":
    unittest.main()
