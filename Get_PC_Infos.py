import platform, os, subprocess, re, sys
import psutil

def Get_CPU_NAME():  ## Return CPU Name depending on which platform the program is Used
     if platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        cpu_name = os.popen('sysctl -n machdep.cpu.brand_string').read()
        cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
        cpu_load = int(cpu_load)
        print('cpu name : {} \ncpu load : {}'.format(cpu_name, cpu_load))
        print(psutil.cpu_percent())


Get_CPU_NAME()