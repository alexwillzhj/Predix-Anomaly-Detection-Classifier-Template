#Predix-Anomaly-Detection-Classifier-Template

A python-based sample analytic that detect abnormal events based on classification method, e.g., QDA classifier.

## Pre-requisites
To run this analytic locally, you will need to have the following:
- Python 2.7+
- Flask 0.10+

## Building, deploying and running the analytic
1. Zip the contents of this directory
2. Create an analytic in Analytics Framework with the name "demo-timeseries-anomaly-detection-classifier-py" and the version "v1".
3. Upload the zip file and attach it to the created analytic.
4. Deploy and test the analytic on Predix Analytics platform.

## Running by Orchestration & Job scheduler after deploying the analytic
1. Upload provided template file as another artifact file in analytic and deploy/valiate the analytic again
2. Use the provided bpmn file with updated analytic ID and name in Orchestration
3. Use the provided port-to-field-map file for the definition of input & output

## Input format
1. AnalyticPython/testbench/data/inputData/analytic_input_train.json for training data
2. AnalyticPython/testbench/data/inputData/analytic_input_test.json for testing data

## Developing a Python-based analytic
1. Implement the analytic (and test functions) according to your development guidelines.
2. Create an entry method in your analytic class. The entry method signature must be in one of the following two formats:
 * For analytics that do not use trained models, use the following signature for your entry method:
  `def entry_method(self, inputJson):`
 * For analytics that use trained models, use the following signature for your entry method:
  `def entry_method(self, inputJson, inputModels):`
 * In either case, the `entry_method` can be any method name. `inputJson` is the JSON string input that will be passed to the analytic. The output of this method must also be a JSON string.
 * `inputModels` contains a dict() of trained models as defined in the port-to-field map. The entry method should properly handle the case of an empty dict.
3. Create a config.json file in the top level of the project directory. Specify the entry method in the format of `<subdirectory>.<className>.<methodName>`, conda-libs, and non-conda-libs.
4. Package all the analytic files and the config.json file into a ZIP file.

For more information, email auther: Alex Zhang (alexwillzhj@gmail.com or alex.zhang@ge.com)
