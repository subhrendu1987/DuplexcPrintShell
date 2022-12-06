current_dir = $(shell pwd)
install:
	ln -s ./DuplexPrint.py /usr/local/bin/duplxprint.py
purge:
	rm /usr/local/bin/duplxprint.py
