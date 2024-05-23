"""
A python Script that reads for a process command in a config file
and starts the command if not running, with the ability to attempt
to restart the command if the exit status is other than 0
"""

import subprocess
import time
import logging

logger = logging.getLogger(__name__)

def load_config(config_file):
    """
    reads a configuration file formatted like an INI file.
    iterate over each line,stores command as a key-value pair
    returns its contents as a dictionary. 
    """
    config = {}
    with open(config_file, 'r') as file:
        lines = file.readlines()
        process_name = None
        for line in lines:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                process_name = line[1:-1]
                config[process_name] = {}
            elif "=" in line and process_name:
                key, value = line.split("=", 1)
                config[process_name][key.strip()] = value.strip()
    return config

def supervisor(process_cmd):
    """
   starts the given command from the config file in a subprocess and monitors its execution. 
   If the subprocess exits with an error, restarts the process. 
   The function logs the status of the process execution.
    """
    logger.info('Supervisor program in progress')
    while True:
        print(f"Starting process: {' '.join(process_cmd)}")
        logger.info('Process %s running', process_cmd)
        process = subprocess.Popen(process_cmd, shell=True)  # Use shell=True for Windows
        process.wait()
        if process.returncode == 0:
            print("Process exited normally")
            logger.info('Process execution successful ')
            break
        else:
            print("Process exited with error. Restarting...")
            logger.info('Process execution failed. Restarting..')
            time.sleep(1)  # Wait for 1 second before restarting

def main():
    """main function""" 
    config_file = "config.ini"
    config = load_config(config_file)
    logging.basicConfig(filename='supervisor.log', level=logging.INFO)

    for process_name, process_config in config.items():
        process_cmd = process_config.get("command")
        if process_cmd:
            process_cmd = process_cmd.split()
            supervisor(process_cmd)

if __name__ == "__main__":
    main()
