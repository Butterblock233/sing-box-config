import json

import json5

import group

"""
You can use this file to check , edit , or delete anything you like in config.jsonc
"""
with open("config.jsonc", "r",encoding='utf-8') as file:
	config_data = json5.load(file)
	
config_data["outbounds"] += [group.japan_group(config_data)]
config_data["outbounds"] += [group.america_group(config_data)]

json.dump(config_data["outbounds"],
				open("draft.jsonc", "w",encoding='utf-8'),
				  indent=4,
				  ensure_ascii=False)