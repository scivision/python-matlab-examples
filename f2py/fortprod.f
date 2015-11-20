!       Note I didn't use normal programming practice like Implicit None
!       to show that it's only INTENT that matters.

        Subroutine ProdNoIntent(x,y,z)
!       This subroutine will not pass result back to Python,
!       since f2py assumes INTENT(IN) instead of INTENT(INOUT) like
!       plain FORTRAN compilers
        z = x * y

        End Subroutine


        Subroutine ProdIntent(x,y,z)
!       This subroutine will pass result back to Python
!       Note that intent(in) is not invincible, subroutines called by
!       subroutines can modify the original variable in the 2nd subroutine
!       doesn't have intent(in)
        Intent(In) :: x,y
        Intent(Out):: z

        z = x * y

        End Subroutine


        Subroutine ProdInOut(x,y,z)
!       This subroutine will pass result back to Python, but requires
!       pre-declaration of z in Python (to any numeric value in this case)
        Intent(In) :: x,y
        Intent(inout)  :: z
!       note: next line is to fix a bug in Numpy 1.9, 1.10 (possibly others) where f2py is not
!       honoring the intent(inout) in the fortran code, intent(inout) or intent(in out) in comment. 
!       It must be cf2py intent(in,out) or !f2py intent(in,out)
        z = x * y

        End Subroutine
        
        Pure Function prodpure(x,y)
!       Pure functions require intent declaration
        Intent(in) :: x,y
        
        prodpure = x*y
        
        End Function