#include <stdio.h>
#include <tetris.h>
#include <def.h>
#include <keyboard.h>
#include <stdlib.h>

void draw_element(int x, int y, int c)
{
	x *= 2;

	printf("\033[%d;%dH", y, x);
	printf("\033[3%dm\033[4%dm", c, c);
	printf("[]");
	fflush(stdout);
	printf("\033[?25l");
	printf("\033[0m");
}

void draw_shape(int x, int y, struct shape p, int c)
{
	for (int i=0; i<5; i++) {
		for (int j=0; j<5; j++) {
			if ( p.s[i][j] != 0 ) {
				draw_element(x+j, y+i, c);
			}
		}
	}
}

int can_move(int x,int y,struct shape p)
{
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            if(p.s[i][j] == 0)
                continue;
            if(x+j >= W)
                return 0;
            if(x+j <0)
                return 0;
            if(y+i >= H)
                return 0;
        }
    }

    return 1;
}

void timer_tetris(struct data *p)
{
	draw_shape(p->x, p->y, shape_arr[0], BC);
    if(can_move(p->x,p->y+1,shape_arr[0]))
    {
	    p->y++;
    }
    else
    {
        p->x=0;
        p->y=0;
    }
	draw_shape(p->x, p->y, shape_arr[0], FC);
}

static struct shape turn_90(struct shape p)
{
	struct shape t;

	for (int i=0; i<5; i++) {
		for (int j=0; j<5; j++) {
			t.s[i][j] = p.s[4-j][i];
		}
	}
	
	return t;
}

void tetris(struct data *p)
{
	int c = get_key();

	if ( is_left(c) ) {
		draw_shape(p->x, p->y, shape_arr[0], BC);
		p->x--;
		draw_shape(p->x, p->y, shape_arr[0], FC);
	}
	if ( is_right(c) ) {
		draw_shape(p->x, p->y, shape_arr[0], BC);
		p->x++;
		draw_shape(p->x, p->y, shape_arr[0], FC);
	}
	if ( is_up(c) ) {
		draw_shape(p->x, p->y, shape_arr[0], BC);
		struct shape t = turn_90(shape_arr[0]);
		shape_arr[0] = t;
		draw_shape(p->x, p->y, shape_arr[0], FC);
	}
	if ( is_down(c) ) {
		draw_shape(p->x, p->y, shape_arr[0], BC);
		p->y++;
		draw_shape(p->x, p->y, shape_arr[0], FC);
	}
	if ( is_esc(c) ) {
		printf("\033[?25h");
		recover_keyboard();
		exit(0);
	}
}

