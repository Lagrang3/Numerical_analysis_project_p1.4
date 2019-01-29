CC=gcc
default: libdist.so

%.so: %.c
	$(CC) $< -o $@ -shared -fpic 
	
check: libdist.so
	./test.py

clean:
	rm *.so
	
.PHONY: clean default check
