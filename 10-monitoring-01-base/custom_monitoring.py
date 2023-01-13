#! /usr/bin/python3

import os
from datetime import datetime
import time
import json

def gen_filename():
    date_stamp = datetime.today().strftime('%y-%m-%d')
    logname = date_stamp + '-awesome-monitoring.log'
    return logname

def cpu_la():
    with open('/proc/loadavg', 'r') as f:
        all_line = f.readlines()
        for line in all_line:
            la = {'LA_for_1min': float(line.split(' ')[0]), 'LA_for_5min': float(line.split(' ')[1]), 'LA_for_15min': float(line.split(' ')[2])}
    return(la)

def meminfo():
    mem_dict = {}
    mem_list = ['MemTotal:', 'MemAvailable:', 'SwapFree:']
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            for mem_i in mem_list:
                if mem_i in line:
                    mem_dict[line.split(':')[0]] = int((line.split(':')[1].strip().split()[0]))
    return(mem_dict)

def disk_info():
    st = os.statvfs('/')
    total_space = st.f_blocks * st.f_frsize
    free_space = st.f_bavail * st.f_frsize
    disk_dict = {'Total_Disk_Space': total_space, 'Free_Disk_Space': free_space, 'Free inodes': st.f_ffree}
    return(disk_dict)

if __name__ == '__main__':
        metric_dict = {'Timestamp': int(time.time()), 'CPU': cpu_la(), 'Memory': meminfo(), 'Disk': disk_info()}
        with open('/var/log/' + gen_filename(), 'a') as file:
            json.dump(metric_dict, file)
            file.write('\n')