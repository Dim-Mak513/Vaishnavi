#include <stdio.h>
#include <stdlib.h>
int main()
{
    //0=rock,1=paper,2=scissor,3=exit
    int a,b,i=1;
    int count = 0,down=0;
    while (i<=5)
    {
        printf("\nenter your move 0=rock,1=paper,2=scissor,3=exit \n");
        scanf("%d",&a);
        b=rand()%3;
        if (a==3)
        {
            exit(1);
        }
        else if(a==0 && b==1)
        {
            printf("\nyou lost\n");
            i++;
            down++;
        }
        else if(a==0 && b==2)
        {
            printf("\nyou won\n");
            i++;
            count++;
        }
        else if(a==1 && b==0)
        {
            printf("\nyou won\n");
            i++;
            count++;
        }
        else if(a==1 && b==2)
        {
            printf("\nyou lost\n");
            i++;
            down++;
        }
        else if(a==2 && b==0)
        {
            printf("\nyou lost\n");
            i++;
            down++;
        }
        else if(a==2 && b==1)
        {
            printf("\nyou won\n");
            i++;
            count++;
        }
        
        else if(a==0 && b==0 || a==1 && b==1 || a==2 && b==2)
        {
            printf("\ndraw\n");
            i++;
        }
        else
        {
            printf("\ndraw\n");
            i++;
        }
    }
    
    if (count>down){
        printf("\nover all you won\n");
    }
    else{
        printf("\nover all you lost\n");
    }
    return 0;
    
    
}