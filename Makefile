.PHONY=ALL clean src rule-set

ALL:build-src build-rule-set
build-src:
	@echo "Building src"
	@make -C src
	@echo "Done"
build-rule-set:
	@echo "Building rule-set"
	@make -C rule-set
	@echo "Done"
clean:
	@make clean -C rule-set
	@make clean -C src