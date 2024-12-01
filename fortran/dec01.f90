subroutine dec01()
use stdlib_io
use stdlib_sorting, only: sort

implicit none

integer :: u ! file reading buffer
integer :: m,n,i,k
integer :: part1=0
integer :: part2=0

integer, allocatable :: x(:, :)
integer, allocatable :: l1(:), l2(:)

!===============================
    write(*,"(/,A,/,A)") "Dec 01","=========================="

    u = open("inputs/input_dec01", "rt")

    ! Works if I know length in advance... is there a workaround for flexibility?
    ! Second column is also six digits but I needed I7 to not clip...???
    call loadtxt("inputs/input_dec01", x, fmt="(I6   I7)")
    !
    close(u)
    m = size(x,dim=1)
    n = size(x,dim=2)

    ! part 1
    allocate(l1(m), l2(m))
    l1 = x(:,1)
    l2 = x(:,2)

    call sort(l1)
    call sort(l2)
    do i=1,m
        part1 = part1 + abs(l1(i) - l2(i))
    end do
    write(*,"(A,I12)") "part 1: ",part1

    !=======================
    ! part 2
    k=1
    do i=1,m
        n=0 ! multiplier
        do while (l2(k) <= l1(i))
            if (l2(k) == l1(i)) then
                n = n + 1
            end if
            k = k + 1
            if (k == m) then
                exit ! inner only!
            end if
        end do
        part2 = part2 + n*l1(i)
        if (k == m) then
            exit
        end if
    end do
    write(*,"(A,I12)") "part 2: ",part2

end subroutine dec01

