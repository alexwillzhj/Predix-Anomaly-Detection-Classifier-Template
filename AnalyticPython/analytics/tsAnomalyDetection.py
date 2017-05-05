import time
import json
import cPickle as pickle
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import numpy as np

class tsAnomalyDetection():

    def __init__(self):
        print "Create python demo for time series anomaly detection"

    def ts_detection(self, data, modelmap = {}):

        # obtain data
        try:
            data_json = json.loads(data)
            ts_curr = data_json['data']['time_series']['feature']
            timestamps = data_json['data']['time_series']['time_stamp']
        except:
            res = -1
            timestamps = [0]
            return json.dumps({"data": {"time_series": {"time_stamp": [timestamps[0]], "detect_res0": [res]}}})

        # obtain model
        try:
            # obtain model in predix environment (model in the same folder)
            try:
                # load classifier
                model_file = open('/home/vcap/app/analytics/qda.pkl', 'r')
                qda = pickle.load(model_file)
                model_file.close()

            # obtain model in local environment (model in the same folder)
            except:
                #load classifier
                model_file = open('qda.pkl', 'r')
                qda = pickle.load(model_file)
                model_file.close()

        except:
            res = -2
            timestamps = [0]
            return json.dumps({"data": {"time_series": {"time_stamp": [timestamps[0]], "detect_res0": [res]}}})

        # classify data
        try:
            # classify
            y_pred = qda.predict(ts_curr[0])

            # assign result to be either 5 (abnormal) or -5 (normal)
            res = y_pred[0] * 10 - 5

        except:
            res = -3
            return json.dumps({"data": {"time_series":{"time_stamp": [timestamps[0]], "detect_res0": [res]}}})

        return json.dumps({"data": {"time_series":{"time_stamp": [timestamps[0]], "detect_res0": [res]}}})

    def ts_training(self, data, modelmap={}):

        model_res = 1

        # data input
        try:
            data_json = json.loads(data)
            ts = data_json['data']['time_series']['feature']
            label = data_json['data']['time_series']['label']

        except:
            model_res = -1
            return model_res

        try:
            qda = QuadraticDiscriminantAnalysis(store_covariances=False, priors=(0.9, 0.1))
            X = np.array([ts])
            qda.fit(X.transpose(), label)

            output = open('qda.pkl', 'wb')
            # Pickle dictionary using protocol 0.
            pickle.dump(qda, output)
            output.close()

        except:
            model_res = -2

        return model_res
