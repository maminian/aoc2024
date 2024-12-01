subroutine dec02()
! imports
use stdlib_io
use stdlib_sorting, only: sort

implicit none

integer :: u ! file reading buffer

!===============================
    write(*,"(/,A,/,A)") "Dec 02","=========================="
    u = open("inputs/input_dec01", "rt")
    !
    !
    
    close(u)

end subroutine dec02
