 all: 
	@while [ -z "$$CONTINUE" ]; do \
	read -r -p "write Y or other char " CONTINUE; \
	done; \
	[ $$CONTINUE = "Y" ] || (echo "not valid"; exit 1;)
	@echo "success"

