#include <sys/timerfd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/select.h>
#include <stdint.h>
#include <unistd.h>

#include <tetris.h>
#include <def.h>
#include <keyboard.h>

int main( void )
{
	int tfd = -1;
	int maxfd;
	int y = 1;
	int x = 1;
	fd_set rset;

	init_keyboard();

	tfd = timerfd_create(CLOCK_MONOTONIC,TFD_CLOEXEC|TFD_NONBLOCK);
	if ( tfd == -1 ) perror("timerfd_create"),exit(EXIT_FAILURE);

	struct itimerspec is;
	memset(&is, 0x00, sizeof is);
	is.it_value.tv_nsec = 1;
	is.it_interval.tv_sec = 1;
	timerfd_settime(tfd, 0, &is, NULL);

	int kfd = fileno(stdin);
	
	maxfd = (tfd>kfd ?tfd:kfd) + 1;
	while ( 1 ) {
		FD_ZERO(&rset);
		FD_SET(tfd, &rset);
		FD_SET(kfd, &rset);

		int nready = select(maxfd, &rset, NULL, NULL, NULL);
		if ( nready <= 0 ) continue;

		if ( FD_ISSET(tfd, &rset) ) {
			uint64_t clk;
			read(tfd, &clk, sizeof clk);
			timer_tetris(&t);
		}
		if ( FD_ISSET(kfd, &rset) ) {
			tetris(&t);
		}
	}

	recover_keyboard();
}

