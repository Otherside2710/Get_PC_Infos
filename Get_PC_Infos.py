import platform, os, subprocess, re, sys
import psutil

monitoring = ()

def get_cpu_usage_pct(): ## Return cpu load

    return psutil.cpu_percent(interval=0.5)

def Get_stats():  ## Return CPU Name depending on which platform the program is Used
    # if platform.system() == "Darwin":
     #   os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        cpu_name = os.popen('sysctl -n machdep.cpu.brand_string').read()
        cpu_name = cpu_name.replace('\n', '\",')
        cpu_Name = cpu_name
        cpu_load = get_cpu_usage_pct()
        cpu_load = str(cpu_load)
        Available_memory = psutil.virtual_memory().available / (1024.0 **3)
        Available_memory = '%.2f' % Available_memory
        myjson = open("stats.json", "w+")
        myjson.write("{\n  \"Statistics\": {")
        myjson.write("\n    \"Cpu_name\": \"{}".format(cpu_Name))
        myjson.write("\n    \"Cpu load\": \"" + cpu_load + "%\",")
        myjson.write("\n    \"Available memory\": \"" + Available_memory + " Go\",")
        myjson.write("\n    \"Total memory\": \"{} Go\"".format(psutil.virtual_memory().total / (1024.0 ** 3)))
        myjson.write("\n    }")
        myjson.write("\n}")

Get_stats()
