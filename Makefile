INC=/usr/local/ssl/include/
LIB=/usr/local/ssl/lib

all:
	gcc -I$(INC) -L$(LIB) -o weakCollision.c -lcrypto -ldl
