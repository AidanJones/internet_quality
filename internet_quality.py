import pyspeedtest
import argparse
import pandas as pd
import numpy as np
import json
import math
import csv
import datetime
import time

#python ~/repos/internet_quality/internet_quality.py -u admin -p admin -o ~/Documents/test.csv

def speed_test():
    #Uses Speedtest.net servers
    print('Starting speed test')
    st = pyspeedtest.SpeedTest(host='quartz.hns.net:8080')
    #http://quartz.hns.net:8080/upload?nocache=4804d89e-6eb8-4149-b046-f31071c6fa96
    #st.host(st,'http://quartz.hns.net:8080')
    ping = st.ping() #ms
    download_bps = st.download()
    download_mbps = download_bps * 10**-6
    upload_bps = st.upload()
    upload_mbps = upload_bps * 10**-6
    return [ping,download_bps,download_mbps,upload_bps,upload_mbps]

def run_speed_test_and_router_check(user,password,output):
    columns=['time_stamp','ping', 'download_bps', 'download_mbps', 'upload_bps', 'upload_mbps']
    df = pd.DataFrame(columns=columns)

    for i in range(5):
        row = [datetime.datetime.now().isoformat()]
        #speed_test_results = speed_test()
        speed_test_results = [39.75844383239746, 9370720.147709526, 9.370720147709525, 1098058.9129463232, 1.0980589129463232]
        row = row + speed_test_results
        print(speed_test_results)
        df2 = pd.DataFrame(data = [row], columns=columns)
        df = df.append(df2,ignore_index=True)
        df.to_csv(output, index=False, quoting=csv.QUOTE_NONNUMERIC)
        time.sleep(60 * 10)

    # https://github.com/KreXor/TP-Link-API/blob/master/tplink.py

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script to record internet speed and router stats")
    parser.add_argument("-u", "--user", help="Router user")
    parser.add_argument("-p", "--password", help="Router password")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    run_speed_test_and_router_check(args.user, args.password, args.output)
