#!/usr/bin/env python3

import setproctitle
import sys
import subprocess
import time

checkTimerInSeconds = 1
configFileLocation = "/etc/bluealsaaplay.conf"
#configFileLocation = "/tmp/bluealsaaplay.conf"

if __name__ == "__main__":
    setproctitle.setproctitle("bluealsaautofix")

    while True:
        #result = subprocess.run(["moodeutl", "-q", "'select value from cfg_system where param='wrkready''"], stdout=subprocess.PIPE)
        result = subprocess.run(["echo", "1"], stdout=subprocess.PIPE)
        resultAsString = result.stdout.decode('utf-8')

        if resultAsString == "1\n":
            print("startup has completed")

            with open(configFileLocation, "w") as configFile:
                configFile.write("AUDIODEV=alsaequal\n")
                configFile.write("BUFFERTIME=500000\n")

            print("configured blue alsa aplay successfully, exiting")            
            sys.exit(0)
        elif resultAsString == "0\n":
            print("startup has not yet completed, waiting for it to happen")
            time.sleep(1)
        else:
            sys.stderr.write(f"got unexpected result '{resultAsString}', exiting")
            sys.exit(1)