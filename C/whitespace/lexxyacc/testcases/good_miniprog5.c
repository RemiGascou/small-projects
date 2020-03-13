main (int args) {
  int c,a = 10;
  int d = 17;
  int b = 1;
  b = a + d;
  c = 4;
  printf(b);
  printf(a);
  while (a) {
    d = d + 1;
    a = a - 1;
    printf(a);
    if (c) {
      printf(c);
    }
    c = c - 2;
  }
  printf(a);
  printf(d);
  d = 24;
  printf(d);
}
