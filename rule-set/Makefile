.PHONY=clean
SC=sing-box rule-set compile

SOURCE=proxy.srs
ALL:$(SOURCE)
%.srs:%.jsonc
	$(SC) $< -o $@
clean:
	rm -rf *.srs