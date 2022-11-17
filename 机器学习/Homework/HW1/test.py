import os
import pandas as pd
from geopy.distance import geodesic


def eval_model(test_path):
    gt = pd.read_csv(os.path.join(test_path, "Location.csv"))
    pred = pd.read_csv(os.path.join(test_path, "Location_output.csv"))
    dist_error = get_dist_error(gt, pred)
    dir_error = get_dir_error(gt, pred)
    print("Distances error: ", dist_error)
    print("Direction error: ", dir_error)


def get_dir_error(gt, pred):
    dir_list = []
    for i in range(int(len(gt) * 0.1), len(gt)):
        dir = abs(gt[gt.columns[5]][i] - pred[pred.columns[5]][i])
        dir_list.append(dir)
    error = sum(dir_list) / len(dir_list)
    return error


def get_dist_error(gt, pred):
    print("local_error")
    dist_list = []
    for i in range(int(len(gt) * 0.1), len(gt)):
        dist = geodesic((gt[gt.columns[1]][i], gt[gt.columns[2]][i]), (pred[pred.columns[1]][i], pred[pred.columns[2]][i])).meters
        dist_list.append(dist)
    error = sum(dist_list) / len(dist_list)
    return error


if __name__ == "__main__":
    eval_model("test_case0")
