import json
import subprocess
import json5
import group
provider_link="***REMOVED***"

def update_providers(profile_link,profile_path, config_path,output_path):
	"""Downloads a provider profile from a given link, and updates a config.jsonc with the outbounds from the downloaded provider profile
	
	Args:
		profile_link (str): URL of the provider profile
		profile_path (str): Path to save the downloaded provider profile
		config_path (str): Path to the config.jsonc to update
	"""
	#subprocess.run(["curl", "-o",profile_path,profile_link])
	with open(profile_path, "r",encoding='utf-8') as file:
		profile_data = json5.load(file)
	with open(config_path, "r",encoding='utf-8') as file:
		config_data = json5.load(file) #Use json5 library to load config.jsonc
	# Update outbound_providers
	config_data['outbounds'] = profile_data['outbounds']
	# Do some extra edits
	config_data['outbounds'][0]['default'] = "日本"
	config_data['outbounds'][0]['outbounds'] += ["日本"]
	config_data['outbounds'][0]['outbounds'] += ["美国"]

	# Append groups
	config_data["outbounds"] += [group.japan_group(config_data)]
	config_data["outbounds"] += [group.america_group(config_data)]
	#Write updated config to config.jsonc
	with open(output_path,'w',encoding='utf-8') as file:
		json5.dump(config_data, file, 
			 indent=4,
			 ensure_ascii=False,
			 quote_keys=True,
			 trailing_commas=False,
			 separators=(',', ': '))
# get_profile(provider_link,"profile.json")
update_providers(provider_link,"profile.json","config.jsonc","../config.jsonc")