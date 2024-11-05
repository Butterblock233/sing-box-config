import json
import json5
import argparse
"""
in this moudle,rule-set is simplily called `rs`
"""
def update_rs(rs_path,config_path):
	with open(rs_path, "r",encoding='utf-8') as file:
		rs = json5.load(file)
	file_name_no_extension = rs_path.split("/")[-1].split(".")[0]
	with open(config_path, "r",encoding='utf-8') as file:
		config_data = json5.load(file)
	#rs_definition
	rs_definition={
		'tag': file_name_no_extension,
		'type':'local',
		'format':'binary',
		"path": "rule-set/{file_name_no_extension}.srs".format(file_name_no_extension=file_name_no_extension),
	}
	config_data['route']['rule_set']+=[rs_definition]
	#rs_rules
	outbound=rs['outbound']
	del rs['outbound']
	rs_rules={
		'rule_set': file_name_no_extension,
		'outbound': outbound
	}
	config_data['route']['rules']+=[rs_rules]
	with open(config_path,'w',encoding='utf-8') as file:
		json.dump(config_data, file,indent=4,ensure_ascii=False,)


def format_rs(rs_path,config_path):
	with open(rs_path, "r",encoding='utf-8') as file:
		rs = json5.load(file)
		file_name_no_extension = rs_path.split("/")[-1].split(".")[0]
	#rs_rules
	outbound=rs['outbound']
	del rs['outbound']
	with open(file_name_no_extension+".json", 'w', encoding='utf-8') as file:
		json.dump(rs, file, indent=4, ensure_ascii=False)



parser = argparse.ArgumentParser(description='Update-rs')
parser.add_argument('--rs_path', help='Path to the rule-set')
parser.add_argument('--config_path', help='Path to the config.jsonc')

args = parser.parse_args()
update_rs(args.rs_path,args.config_path)
format_rs(args.rs_path,args.config_path)
