import platform, os, subprocess, re, sys
import psutil

monitoring = ()

def get_cpu_usage_pct(): ## Return cpu load

    return psutil.cpu_percent(interval=0.5)

def Get_stats():  ## Return CPU Name depending on which platform the program is Used
    # if platform.system() == "Darwin":
     #   os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        cpu_name = os.popen('sysctl -n machdep.cpu.brand_string').read()
        cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
        cpu_load = int(cpu_load)
        print('cpu name : {}cpu load : {}%'.format(cpu_name, get_cpu_usage_pct()))
        print('Total memory : {} Go'.format(psutil.virtual_memory().total / (1024.0 ** 3)))
        Available_memory = psutil.virtual_memory().available / (1024.0 **3)
        print('Available memory : ' + '%.2f' % Available_memory + ' Go')

Get_stats()
