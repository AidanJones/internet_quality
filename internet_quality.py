import pyspeedtest
import argparse
import pandas as pd
import numpy as np
import json
import math
import csv

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
    speed_test_results = speed_test()
    print(speed_test_results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script to record internet speed and router stats")
    parser.add_argument("-u", "--user", help="Router user")
    parser.add_argument("-p", "--password", help="Router password")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    run_speed_test_and_router_check(args.user, args.password, args.output)
