INSTALL_PATH = /usr/bin
PROGRAM_NAME = minifetch

install:
	cp ./bin/$(PROGRAM_NAME) $(INSTALL_PATH)
	$(SILENT)echo "Minifetch successfully installed!"

repair:
	rm -f $(INSTALL_PATH)/$(PROGRAM_NAME) 
	$(SILENT)echo "Minifetch successfully removed!"
	cp ./bin/$(PROGRAM_NAME) $(INSTALL_PATH)
	$(SILENT)echo "Minifetch successfully repaired!"

uninstall:
	rm -f $(INSTALL_PATH)/$(PROGRAM_NAME) 
	$(SILENT)echo "Minifetch successfully removed!"
