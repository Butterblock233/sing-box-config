.PHONY=clean
SC=sing-box rule-set compile

SOURCE=$(subst .jsonc,.srs,$(wildcard *.jsonc))
ALL:$(SOURCE) clean-json
%.srs:%.jsonc 
	@python ../src/update_rs.py --rs_path=$< --config_path=../config.jsonc
	@$(SC) $(subst .jsonc,.json,$<) -o $@
	@echo "Building $@"
clean-json:
	@rm -rf *.json
clean:clean-json
	rm -rf *.srs