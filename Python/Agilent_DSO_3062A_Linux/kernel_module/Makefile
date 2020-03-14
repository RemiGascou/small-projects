.PHONY : all clean build_kernel_module test

MODULE := src/agilent_dso_3000_usb.c

#=============================================================s

obj-m += $(patsubst %.c,%.o,$(MODULE))
MODULENAME := $(patsubst %.c,%,$(shell basename $(MODULE)))
BINDIR := $(shell dirname $(shell dirname $(MODULE)))/bin/
SRCDIR := $(shell dirname $(MODULE))/

all: clean build_kernel_module

build_kernel_module:
	if [ ! -d $(BINDIR) ]; then mkdir -p $(BINDIR); fi
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)
	@if [ -f "$(SRCDIR)$(MODULENAME).ko" ]; then cp "$(SRCDIR)$(MODULENAME).ko" "$(BINDIR)$(MODULENAME).ko"; fi

clean :
	@if [ -f "$(SRCDIR)$(MODULENAME).mod.c" ]; then 	    rm "$(SRCDIR)$(MODULENAME).mod.c"; 	     fi
	@if [ -f "$(SRCDIR)$(MODULENAME).o" ]; then 		    rm "$(SRCDIR)$(MODULENAME).o"; 		     fi
	@if [ -f "$(SRCDIR)$(MODULENAME).order" ]; then 	    rm "$(SRCDIR)$(MODULENAME).order"; 	     fi
	@if [ -f "$(SRCDIR)$(MODULENAME).ko" ]; then 		    rm "$(SRCDIR)$(MODULENAME).ko"; 		 fi
	@if [ -f "$(SRCDIR)$(MODULENAME).mod.o" ]; then 	    rm "$(SRCDIR)$(MODULENAME).mod.o"; 	     fi
	@if [ -f "$(SRCDIR).$(MODULENAME).ko.cmd" ]; then 	    rm "$(SRCDIR).$(MODULENAME).ko.cmd"; 	 fi
	@if [ -f "$(SRCDIR).$(MODULENAME).mod.o.cmd" ]; then 	rm "$(SRCDIR).$(MODULENAME).mod.o.cmd";  fi
	@if [ -f "$(SRCDIR).$(MODULENAME).mod.cmd" ]; then      rm "$(SRCDIR).$(MODULENAME).mod.cmd";    fi
	@if [ -f "$(SRCDIR).$(MODULENAME).o.cmd" ]; then 	    rm "$(SRCDIR).$(MODULENAME).o.cmd"; 	 fi
	@if [ -f "$(SRCDIR)$(MODULENAME).mod" ]; then           rm "$(SRCDIR)$(MODULENAME).mod";         fi
	@if [ -f "$(SRCDIR)modules.order" ]; then 			    rm "$(SRCDIR)modules.order"; 		     fi
	@if [ -f "$(SRCDIR)Module.symvers" ]; then 			    rm "$(SRCDIR)Module.symvers"; 		     fi
	@if [ -d "$(SRCDIR).tmp_versions" ]; then 			    rm -rf "$(SRCDIR).tmp_versions";      	 fi

test:
	# We put a - in front of the rmmod command to tell make to ignore
	# an error in case the module isn't loaded.
	-sudo rmmod "$(MODULENAME)"
	# Clear the kernel log without echo
	sudo dmesg -C
	# Insert the module
	sudo insmod "$(BINDIR)$(MODULENAME).ko"
	# Display the kernel log
	dmesg

uninstall:
	-sudo rm -f /dev/$(MODULENAME)[0-9]
	-sudo rmmod "$(MODULENAME)"
	
install:
	# Remove module from kernel (just in case it is still running)
	-sudo /sbin/rmmod $(MODULENAME)

	# Install module
	sudo /sbin/insmod "$(BINDIR)$(MODULENAME).ko"

	# Find major number used
	$(eval MAJOR_NUM := $(shell cat /proc/devices | grep $(MODULENAME) | awk '{print $$1}'))
	echo "Using major number $(MAJOR_NUM)"

	# Remove old device files
	sudo rm -f /dev/$(MODULENAME)[0-9]

	# Create new device files
	sudo mknod /dev/$(MODULENAME)0 c $(MAJOR_NUM) 0

	# Change access mode (RW access for everybody)
	sudo chmod 666 /dev/$(MODULENAME)0
