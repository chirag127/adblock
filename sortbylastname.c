#include<stdio.h>
#include<string.h>



void main(){
   int i,j,n;
   char str[100][100],s[100];
   printf("Enter number of names :\n");
   scanf("%d",&n);
   printf("Enter names in any order:\n");
   for(i=0;i<n;i++){
      scanf("%s",str[i]);
   }
   for(i=0;i<n;i++){
      for(j=i+1;j<n;j++){
         if(strcmp(str[i],str[j])>0){
            strcpy(s,str[i]);
            strcpy(str[i],str[j]);
            strcpy(str[j],s);
         }
      }
   }
   printf("\nThe sorted order of names are:\n");
   for(i=0;i<n;i++){
      printf("%s\n",str[i]);
   }
}
