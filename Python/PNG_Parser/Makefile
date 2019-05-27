all : clean

test:
	@python3 lib/main_tests.py

clean :
	@if [ `find ./ -type d -name "*__pycache__" | wc -l` != 0 ] ;	then rm -rf `find ./ -type d -name "*__pycache__"` ; fi;
