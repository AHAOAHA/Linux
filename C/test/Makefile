test:test.c
	gcc -E test.c -o test.i
	gcc -S test.i -o test.s
	gcc -c test.s -o test.o
	gcc test.o -o test
.PHONY:clean
clean:
	rm -f test.i test.s test.o test
