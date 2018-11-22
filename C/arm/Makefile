.PHONY:all
all:common_div date is_leapyear main
common_div:common_div.c
	gcc $^ -o $@
date:date.c
	gcc $^ -o $@
is_leapyear:is_leapyear.c
	gcc $^ -o $@
main:main.c
	gcc $^ -o $@ 

.PHONY:clean
clean:
	rm -f common_div date is_leapyear main
