# coding:utf-8
import os
import csv

#Record data from html to csv file
def write_csv(data):
    datas = [data]
    with open(os.getcwd()+'/ml/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(datas)