MODULE := lkm_example.c

obj-m += lkm_example.o

all: clean build_kernel_module build_user

build_kernel_module:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)

build_user:
	gcc -Wall helloWorld.c -I helloWorld.h -o helloWorld

clean :
	@if [ -f "$(patsubst %.c,%,$(MODULE)).mod.c" ]; then 	rm "$(patsubst %.c,%,$(MODULE)).mod.c"; 	fi
	@if [ -f "$(patsubst %.c,%,$(MODULE)).o" ]; then 		rm "$(patsubst %.c,%,$(MODULE)).o"; 		fi
	@if [ -f "$(patsubst %.c,%,$(MODULE)).order" ]; then 	rm "$(patsubst %.c,%,$(MODULE)).order"; 	fi
	@if [ -f "$(patsubst %.c,%,$(MODULE)).ko" ]; then 		rm "$(patsubst %.c,%,$(MODULE)).ko"; 		fi
	@if [ -f "$(patsubst %.c,%,$(MODULE)).mod.o" ]; then 	rm "$(patsubst %.c,%,$(MODULE)).mod.o"; 	fi
	@if [ -f ".$(patsubst %.c,%,$(MODULE)).ko.cmd" ]; then 	rm ".$(patsubst %.c,%,$(MODULE)).ko.cmd"; 	fi
	@if [ -f ".$(patsubst %.c,%,$(MODULE)).mod.o.cmd" ]; then 	rm ".$(patsubst %.c,%,$(MODULE)).mod.o.cmd"; fi
	@if [ -f ".$(patsubst %.c,%,$(MODULE)).o.cmd" ]; then 	rm ".$(patsubst %.c,%,$(MODULE)).o.cmd"; 	fi
	@if [ -f "modules.order" ]; then 						rm "modules.order"; 						fi
	@if [ -f "Module.symvers" ]; then 						rm "Module.symvers"; 						fi
	@if [ -d ".tmp_versions" ]; then 						rm -rf ".tmp_versions";  					fi

modulesclean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)

cleantest:
	# We put a - in front of the rmmod command to tell make to ignore
	# an error in case the module isn't loaded.
	-sudo rmmod lkm_example
	# Clear the kernel log without echo
	sudo dmesg -C
	# Insert the module
	sudo insmod lkm_example.ko
	# Display the kernel log
	dmesg
