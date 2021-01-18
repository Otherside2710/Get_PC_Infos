import platform, os, subprocess, re

def Ascii_Apple():
    

def Get_CPU_NAME():  ## Return CPU Name depending on which platform the program is Used
     if platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        cpu_name = os.popen('sysctl -n machdep.cpu.brand_string').read()
        print('CPU IS : {}'.format(cpu_name))
    


Get_CPU_NAME()