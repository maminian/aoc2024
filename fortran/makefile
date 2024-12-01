STDLIB_CFLAGS := `pkg-config --cflags fortran_stdlib`
STDLIB_LIBS := `pkg-config --libs fortran_stdlib`

# Example definition of Fortran compiler and flags
FC := gfortran
FFLAGS := -O3 -g -Wcharacter-truncation -Wconversion -Wextra -Winteger-division -fbounds-check

# 
SUBROUTINES := dec01.f90 dec02.f90

clean:
	rm -f main
	rm -f *.o

main: main.f90
	$(FC) $(SUBROUTINES) $< -o $@ $(FFLAGS) $(STDLIB_CFLAGS) -lfortran_stdlib

run:
	./main

reset: clean main run

# Example rule to compile object files from .f90 files
%.o: %.f90
	$(FC) -c -o $@ $< $(FFLAGS) $(STDLIB_CFLAGS) -lfortran_stdlib
#$(FFLAGS) $(STDLIB_CFLAGS)
%: %.o
	$(FC) -o $@ $^ $(FFLAGS) $(STDLIB_CFLAGS) -lfortran_stdlib

# If I need a reminder... https://makefiletutorial.com/
#moo: moo.f90
#	$(FC) moo.f90 -o moo
