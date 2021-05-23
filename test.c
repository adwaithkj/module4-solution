#include <stdio.h>
#include <stdlib.h>

int closestelement(int *a)
{
    int closest, i = 0, avg, length;
    closest = abs(*a - avg);
    int result = *a;
    for (i = 1; i < length; i++)
    {
        if (abs(*(a + i) - avg) <= closest)
        {
            closest = abs(*(a + i) - avg);
            result = *(a + i);
        }
    }
    return result;
}
int main()
{
    int *a, length, i, sum = 0, m, avg, ans;
    scanf("%d", &length);
    a = (int *)malloc(length * sizeof(int));
    for (i = 0; i < length; i++)
    {
        scanf("%d", &m);
        *(a + i) = m;
        sum += m;
    }

    printf(" hello %s", a);
    avg = sum / length;
    ans = closestelement(a);
    printf("random shit");

    printf("%d", ans);
    return 0;
}