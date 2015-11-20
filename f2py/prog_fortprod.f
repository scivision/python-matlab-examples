!       gfortran prog_fortprod.f fortprod.f 

        Program prodfort
        
        x=3.
        y=2.

        call prodnointent(x,y,znoint)
        print *, znoint
        
        call prodintent(x,y,zint)
        print *, zint
        
        zinout=-1.
        call prodinout(x,y,zinout)
        print *,zinout
        
        zpure = prodpure(x,y)
        print *,zpure
        
        End Program