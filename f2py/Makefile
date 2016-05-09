SRC=fortprod.f90
MAIN=prog_fortprod.f90
#----------------
FC = gfortran 
F2PY = f2py3

FFLAGS = -std=f2008 -Wall -Wpedantic -Wextra -mtune=native -fexternal-blas -O3


OBJS=$(SRC:.f90=.o)
MOBJS=$(OBJS) $(MAIN:.f90=.o)

%.o: %.f90
	$(FC) $(FFLAGS) -c $<

all: prod.out pyprod

prod.out: $(MOBJS)
	$(FC) -o $@ $(MOBJS) $(FFLAGS)

pyprod: $(SRC)
	$(F2PY) --quiet -m $@ -c $(SRC)

clean:
	$(RM) $(MOBJS)

