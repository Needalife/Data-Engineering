import os

def read_config() -> dict:
    config = {}
    
    config_file_path = os.path.join(os.path.dirname(__file__), "client.properties")
    
    with open(config_file_path) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                config[parameter] = value.strip()

    return config

