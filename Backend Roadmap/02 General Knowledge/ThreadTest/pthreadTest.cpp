#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int sum;                   /* this data is shared by the thread(s) */
void *runner(void *param); /* threads call this function */

int main(int argc, char *argv[])
{
    pthread_t tid;       /* the thread identifier */
    pthread_attr_t attr; /* set of thread attributes */
    if (argc != 2)
    {
        fprintf(stderr, "usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0)
    {
        fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
        return -1;
    }
    /* get the default attributes */
    pthread_attr_init(&attr);
    /* create the thread */
    pthread_create(&tid, &attr, runner, argv[1]);
    /* wait for the thread to exit */
    // pthread_join(tid, NULL);

    sleep(5);

    printf("sum = %d\n", sum);
    printf("main end\n");
}
/* The thread will begin control in this function */
void *runner(void *param)
{
    int i, upper = atoi((char *)param);
    sum = 0;
    printf("pthread Start\n");
    for (i = 1; i <= upper; i++)
    {
        printf("%d\n", i);
        sum += i;
    }
    printf("pthread End\n");
    pthread_exit(0);
}