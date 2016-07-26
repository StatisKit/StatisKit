cc -L$PREFIX/lib -I$PREFIX/include $RECIPE_DIR/test.c -o test.o -lmpfr -lgmp
./test.o
