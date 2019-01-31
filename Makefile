CC=gcc
default: libdist.so pydist.cpython-37m-x86_64-linux-gnu.so 

pydist.cpython-37m-x86_64-linux-gnu.so: pydist.pyx
	python setup.py build_ext -if

libdist.so: libdist.c
	$(CC) $< -o $@ -shared -fpic 
	
check: libdist.so
	./test.py

run: libdist.so
	./init.py

clean:
	rm -r build *.so pydist.c
	
.PHONY: clean default check run
