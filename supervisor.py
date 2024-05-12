import subprocess
import time

def load_config(config_file):
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
    while True:
        print(f"Starting process: {' '.join(process_cmd)}")
        process = subprocess.Popen(process_cmd, shell=True)  # Use shell=True for Windows
        process.wait()
        if process.returncode == 0:
            print("Process exited normally")
            break
        else:
            print("Process exited with error. Restarting...")
            time.sleep(1)  # Wait for 1 second before restarting

def main():
    config_file = "config.ini"
    config = load_config(config_file)

    for process_name, process_config in config.items():
        process_cmd = process_config.get("command")
        if process_cmd:
            process_cmd = process_cmd.split()
            supervisor(process_cmd)

if __name__ == "__main__":
    main()
