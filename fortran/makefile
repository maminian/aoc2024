STDLIB_CFLAGS := `pkg-config --cflags fortran_stdlib`
STDLIB_LIBS := `pkg-config --libs fortran_stdlib`

# Example definition of Fortran compiler and flags
FC := gfortran
FFLAGS := -O3 -Wall -g

# 
SUBROUTINES := hi.f90 dec01.f90

make clean:
	rm main hi dec01 *.o

main: main.f90
	$(FC) $(SUBROUTINES) $< -o $@ $(FFLAGS) $(STDLIB_CFLAGS) 

# Example rule to compile object files from .f90 files
%.o: %.f90
	$(FC) -c -o $@ $< $(FFLAGS) $(STDLIB_CFLAGS)

%: %.o
	$(FC) -o $@ $^ $(FFLAGS) $(STDLIB_LIBS)

# If I need a reminder... https://makefiletutorial.com/
#moo: moo.f90
#	$(FC) moo.f90 -o moo
