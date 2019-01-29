CC=gcc
default: libdist_H.so

%.so: %.c
	$(CC) $< -o $@ -shared -fpic 
	
check: libdist_H.so
	./test.py

clean:
	rm *.so
	
.PHONY: clean default check
