#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define ICPOISON do { x ^= y; } while (0)

#define ICPOISON2      ICPOISON;       ICPOISON
#define ICPOISON4      ICPOISON2;      ICPOISON2
#define ICPOISON8      ICPOISON4;      ICPOISON4
#define ICPOISON16     ICPOISON8;      ICPOISON8
#define ICPOISON32     ICPOISON16;     ICPOISON16
#define ICPOISON64     ICPOISON32;     ICPOISON32
#define ICPOISON128    ICPOISON64;     ICPOISON64
#define ICPOISON256    ICPOISON128;    ICPOISON128
#define ICPOISON512    ICPOISON256;    ICPOISON256
#define ICPOISON1024   ICPOISON512;    ICPOISON512
#define ICPOISON2048   ICPOISON1024;   ICPOISON1024
#define ICPOISON4096   ICPOISON2048;   ICPOISON2048
#define ICPOISON8192   ICPOISON4096;   ICPOISON4096
#define ICPOISON16384  ICPOISON8192;   ICPOISON8192
#define ICPOISON32768  ICPOISON16384;  ICPOISON16384
#define ICPOISON65536  ICPOISON32768;  ICPOISON32768
#define ICPOISON131072 ICPOISON65536;  ICPOISON65536
#define ICPOISON262144 ICPOISON131072; ICPOISON131072

int main(int argc, char **argv) {
  int x = 0xf0;
  int y = 0x0f;

  if (argc != 3) {
    printf("Usage: l1i usr_time intensity\n");
    exit(0);
  }
  
  int usr_timer = atoi(argv[1]);
  printf ("usr_time: %d\n", usr_timer);

  int intensity = atoi(argv[2]);
  if (intensity < 0 || intensity > 20) {
    printf("usr_timer must be an integer between [0..20]\n");
    exit(0);
  }
  printf("intensity: %d\n", intensity);

  clock_t begin, end;
  double time_spent;

  begin = clock();

  //for (int j = 0; j < 10*usr_timer; j++) { 
  for (int j = 0; j < 1500; j++) {
	switch (intensity) {
	    case 0:  for (int i = 0; i < usr_timer; i++) { ICPOISON; } //intensity = 0;
	    case 1:  for (int i = 0; i < usr_timer; i++) { ICPOISON2; } //intensity = 1;
	    case 2:  for (int i = 0; i < usr_timer; i++) { ICPOISON4; } //intensity = 2;
	    case 3:  for (int i = 0; i < usr_timer; i++) { ICPOISON8; } //intensity = 3;
	    case 4:  for (int i = 0; i < usr_timer; i++) { ICPOISON16; } //intensity = 4;
	    case 5:  for (int i = 0; i < usr_timer; i++) { ICPOISON32; } //intensity = 5;
	    case 6:  for (int i = 0; i < usr_timer; i++) { ICPOISON64; } //intensity = 6;
	    case 7:  for (int i = 0; i < usr_timer; i++) { ICPOISON128; } //intensity = 7;
	    case 8:  for (int i = 0; i < usr_timer; i++) { ICPOISON256; } //intensity = 8;
	    case 9:  for (int i = 0; i < usr_timer; i++) { ICPOISON512; } //intensity = 9;
	    case 10: for (int i = 0; i < usr_timer; i++) { ICPOISON1024; } //intensity = 10;
	    case 11: for (int i = 0; i < usr_timer; i++) { ICPOISON2048; } //intensity = 11;
	    case 12: for (int i = 0; i < usr_timer; i++) { ICPOISON4096; } //intensity = 12;
	    case 13: for (int i = 0; i < usr_timer; i++) { ICPOISON8192; } //intensity = 13;
	    case 14: for (int i = 0; i < usr_timer; i++) { ICPOISON16384; } //intensity = 14;
	    case 15: for (int i = 0; i < usr_timer; i++) { ICPOISON32768; } //intensity = 15;
	    case 16: for (int i = 0; i < usr_timer; i++) { ICPOISON65536; } //intensity = 16;
	    case 17: for (int i = 0; i < usr_timer; i++) { ICPOISON131072; } //intensity = 17;
	    case 18: for (int i = 0; i < usr_timer; i++) { ICPOISON262144; } //intensity = 18;
	    case 19: for (int i = 0; i < usr_timer; i++) { ICPOISON262144; } //intensity = 19;
	    case 20: for (int i = 0; i < usr_timer; i++) { ICPOISON262144; } //intensity = 20;
  	}
  }

  end = clock();
  time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time spent: %f\n", time_spent);
  
  return 0;
}
