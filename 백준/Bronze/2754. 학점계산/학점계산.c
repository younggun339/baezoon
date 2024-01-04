#include <stdio.h>


float count(char grade[1],float score) {
    if(grade[1] == '0'){
        score = score - 0.3;}
    else if(grade[1] == '-'){
        score = score - 0.6;
    }
    return score;
}

int main() {
    char grade[1];
    scanf("%s", grade);
    float score;
    // printf("%c",grade[1]);
    // printf("%c", grade[0]);
    if(grade[0] == 'A'){
        score = 4.3;
        // count(grade, score);
        // printf("%c", grade[1]);
        if(grade[1] == '0'){
            score = score - 0.3;}
        else if(grade[1] == '-'){
            score = score - 0.6;
        }
        }
    else if (grade[0] == 'B')
    {
        score = 3.3;
        // count(grade, score);
        if(grade[1] == '0'){
            score = score - 0.3;}
        else if(grade[1] == '-'){
            score = score - 0.6;
        }
    }
    else if (grade[0] =='C')
    {
        score = 2.3;
        // count(grade, score);
        if(grade[1] == '0'){
            score = score - 0.3;}
        else if(grade[1] == '-'){
            score = score - 0.6;
        }
    }
    else if (grade[0] =='D')
    {
        score = 1.3;
        // count(grade, score);
        if(grade[1] == '0'){
            score = score - 0.3;}
        else if(grade[1] == '-'){
            score = score - 0.6;
        }
    }
    else{
        score = 0.0;
        // count(grade, score);
        if(grade[1] == '0'){
            score = score - 0.3;}
        else if(grade[1] == '-'){
            score = score - 0.6;
        }
    }

    printf("%.1f", score);
}