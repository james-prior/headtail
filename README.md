The ht command combines the 
[head](https://en.wikipedia.org/wiki/Head_%28Unix%29)
and [tail](https://en.wikipedia.org/wiki/Tail_%28Unix%29) programs.

NAME

    ht - (headtail) output the beginning and ending of files

SYNOPSIS

    ht [OPTION]... [FILE]...

    Print the beginning and ending of each file.
    Prints '...' for omitted lines.
    Defaults to first 10 and last 10 lines.
    Standard input may be specified by - argument.
    If no file is specified, uses standard input.

    Prints header lines if more than one file.
        Prints a blank line between output of multiple files.

OPTIONS

    -n, --lines=n
        Specify the number of lines from beginning and end of file to print.

    --head-lines=n
        Specify the number of lines from beginning of file to print.

    --tail-lines=n
        Specify the number of lines from end of file to print.

    -v, --verbose
        Print headers.

    -q, --quiet, --silent
        Do not print headers.

    --help
        Show this and quit.

EXAMPLES

    ls -ltr ~ | ht -20
        Shows first 20 and last 20 lines of output of previous command.

    ht --head-lines=1 --tail-lines=3 *.py
        Shows first line and last three lines of each *.py file.
