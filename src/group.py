import json
import re

import json5

with open("config.jsonc", "r",encoding='utf-8') as file:
	config_data = json5.load(file)

def update_groups(config_data, country,type="urltest",alias=[]):
    """return a json like :
    {
    "type": "selector",
    "tag": "<country>",
    "outbounds": [
        "<country> 02 [V3]",
        "<country> 03",
        "<country> 04 [V2]"
    ],
    "interrupt_exist_connections": false
	}
    """
    group = {
        "type": type,
        "tag": country,
        "outbounds": []
    }
    for outbound in config_data["outbounds"]:
        if re.match(rf".*{country}.*", outbound["tag"]):
            group["outbounds"].append(outbound["tag"])
    return group
