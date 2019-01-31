CC=gcc
default: pydist.cpython-37m-x86_64-linux-gnu.so 

pydist.cpython-37m-x86_64-linux-gnu.so: pydist.pyx libdist.c
	python setup.py build_ext -if

#libdist.so: libdist.c
#	$(CC) $< -o $@ -shared -fpic 
	
check: pydist.cpython-37m-x86_64-linux-gnu.so
	./test.py

run: pydist.cpython-37m-x86_64-linux-gnu.so
	./init.py

clean:
	rm -r build *.so pydist.c
	
.PHONY: clean default check run
