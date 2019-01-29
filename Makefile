CC=gcc
default: libdist.so

%.so: %.c
	$(CC) $< -o $@ -shared -fpic 
	
check: libdist.so
	./test.py

run: libdist.so
	./init.py

clean:
	rm *.so 
	
.PHONY: clean default check run
