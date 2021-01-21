import time
import psutil, os

def main():
    old_Upload_volume = 0
    old_Download_volume = 0
    while True:
        Upload_volume = psutil.net_io_counters().bytes_sent
        Download_volume = psutil.net_io_counters().bytes_recv

        if Download_volume:
            send_stat_Upload(Upload_volume - old_Upload_volume)
            send_stat_Download(Download_volume - old_Download_volume)

        old_Upload_volume = Upload_volume
        old_Download_volume = Download_volume

        time.sleep(1)
        os.system('clear')
def convert_to_Mo(value):
    return value/1024./1024.

def send_stat_Download(value):
    print ("Download : " + "%0.3f" % convert_to_Mo(value) + " Mo")

def send_stat_Upload(value):
    print ("Upload :" + "%0.3f" % convert_to_Mo(value) + " Mo")

main()
