test:test.c
    gcc -E test.c -o test.i
	gcc -S test.i -o test.s
	gcc -c test.s -o test
.PHONY:clean
clean:
    rm -f test
	rm -f test.i
	rm -f test.s
