#include <stdio.h>
#include <math.h> // for pow()
#include <time.h> // for time measuring in first loop
#include <stdlib.h> // for atof()
#include <getopt.h> // for getting options in the CLI
#include <unistd.h> // for EXIT_SUCESS, EXIT_FAILURE

#define PI_ARRAY_SIZE 4294
#define TAB "  "
#define OPTSTR "vphd:t:"
#define VERSION_STR "\n%s 1.0\n\nWritten by porbee; @porbee on Github ©\nEscrito por porbee; @porbee en Github ©\n\n<%s>\n"
#define GITHUB_REPO_LINK ""

extern char *optarg;

struct inputted_parameters
{
    float loop_duration;
    unsigned int decimal_print_count;
    unsigned short printing_array_starter;
};

int main(int argc, char * const argv[])
{
    struct inputted_parameters parameter;
    int option;
    opterr = 0;
    while ((option = getopt(argc, argv, "vphd:t:")) != -1)
    {
        switch (option)
        {
        case 'v':
            printf(VERSION_STR, argv[0], GITHUB_REPO_LINK);
            exit(EXIT_SUCCESS);
            break;
        case 'h':
            printf("\n%s -t parameter -d parameter [-v] [-p]\n\n", argv[0]);
            printf("\'-t\' specifies the time in seconds for the calculation process\n");
            printf("\'-d\' specifies how many decimals of pi are outputted\n");
            printf("\'-v\' provides information about the program and the version\n");
            printf("\'-p\' makes the output start with 3,\n");
            exit(EXIT_SUCCESS);
            break;
        case 't':
            parameter.loop_duration = atof(optarg);
            break;
        case 'd':
            parameter.decimal_print_count = atoi(optarg);
            break;
        case 'p':
            parameter.printing_array_starter = 1;
            break;
        default:
            printf("NOT RECOGNIZED");
            exit(EXIT_FAILURE);
        }
    }
    double pi_double_form, k = 0, loop_time = 0;
    unsigned int printing_position = 1, six_digit_separator = 0, appending_position = 0;


    unsigned short pi[PI_ARRAY_SIZE] = {3,};
    double time_previous_loop = ((double) clock()) / CLOCKS_PER_SEC;
    while (loop_time < (parameter.loop_duration + time_previous_loop))
    {
        pi_double_form += ((pow(-1.0, k)) / ((2.0 * k) + 1.0));
        loop_time = ((double) clock()) / CLOCKS_PER_SEC;
        k++;
    }
    pi_double_form *= 4;


    while (appending_position < parameter.decimal_print_count)
    {
        pi[appending_position] = ((unsigned short) pi_double_form);
        pi_double_form -= ((double) pi[appending_position]);
        pi_double_form *= 10.0;
        appending_position++;
    }


    if (parameter.printing_array_starter == 1) {printf("3,");}
    while (printing_position < parameter.decimal_print_count)
    {
        if ((six_digit_separator % 6) == 0 && six_digit_separator > 0)
        {
            printf(TAB);
        }
        printf("%hu", pi[printing_position]);
        printing_position++;
        six_digit_separator++;
    }
    return 0;
}

/*
gcc -lm -Wall -c pi.c && gcc pi.o -lm -Wall -o PI
./PI -t 4 -d 521 && rm PI && rm pi.o

for reference:
                https://www.cecm.sfu.ca/organics/papers/borwein/paper/html/local/billdigits.html
                https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
*/