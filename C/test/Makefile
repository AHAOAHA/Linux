test:test.c
	gcc -E test.c -o test.i -g
	gcc -S test.i -o test.s -g
	gcc -c test.s -o test.o -g
	gcc test.o -o test -g
.PHONY:clean
clean:
	rm -f test.i test.s test.o test
