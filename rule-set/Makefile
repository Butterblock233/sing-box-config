.PHONY=clean
SC=sing-box rule-set compile

SOURCE=$(subst .jsonc,.srs,$(wildcard *.jsonc))
ALL:$(SOURCE) clean-json
%.srs:%.jsonc 
	python update_rs.py --rs_path=$< --config_path=../config.jsonc
	$(SC) $(subst .jsonc,.json,$<) -o $@
clean-json:
	rm -rf *.json
clean:
	rm -rf *.srs *.json