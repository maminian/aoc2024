# aoc2024
advent of code 2024

# huh?
Am I really going to use Fortran? 

...sure. I did it for my thesis. Might be fun to revisit it. 
I'm going to try out the stdlib 
being developed to help things along, though; 
see https://github.com/fortran-lang/stdlib

# Requirements (Fortran)
* https://github.com/fortran-lang/stdlib and associated requirements described within. 
A full installation is expected -- I haven't set up the compiler to look for files locally.
* pkg-config

You should navigate your terminal to the `fortran` folder and compile any day, or all days, with a make command; e.g. `make dec01; ./dec01` would make and run December 1's solution. 
The file `main.f90` will run all day's solutions.

For the Fortran solution, I manually rename the input for the day and throw them all in `fortran/inputs/`; e.g. `input_dec01`.
