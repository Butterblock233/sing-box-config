import json
import re

import json5

with open("config.jsonc", "r",encoding='utf-8') as file:
	config_data = json5.load(file)

def japan_group(config_data):
	matched = ""
	"""return a json like :
	{
	"type": "urltest",
	"tag": "日本",
	"outbounds": [
		"日本 02 [V3]",
		"日本 03",
		"日本 04 [V2]"
	],
	"interrupt_exist_connections": false}
	"""
	group={
	"type": "urltest",
	"tag": "日本",
  	"outbounds": []
	}
	for outbound in config_data["outbounds"]:
		if re.match(r".*日本.*", outbound["tag"]):
			group["outbounds"].append(outbound["tag"])
	return group

def america_group(config_data):
	"""return a json like :
	{
	"type": "urltest",
	"tag": "美国",
	"outbounds": [
		"美国 02 [V3]",
		"美国 03",
		"美国 04 [V2]"
	],
	"interrupt_exist_connections": false}
	"""
	matched = ""
	group={
	"type": "urltest",
	"tag": "美国",
  	"outbounds": []
	}
	for outbound in config_data["outbounds"]:
		if re.match(r".*美国.*", outbound["tag"]):
			group["outbounds"].append(outbound["tag"])
	return group
#print(json.dumps(japan_group(config_data),ensure_ascii=False,indent=4))