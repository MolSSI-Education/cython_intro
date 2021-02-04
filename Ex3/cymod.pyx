from libc cimport math
import cython


@cython.cdivision(True)
cdef double kernel(double x, double width=4.0):
    """Returns the nornalized value of a Gaussian-like function.
    Parameters
    ----------
    x: float
       x-cartesian coordinate
    width: float, optional
       width of the distribution
    """
    cdef double normk = 2.0 / (width * math.sqrt(width * math.pi))
    return normk * x ** 2 * math.exp(-(x ** 2) / width)


@cython.cdivision(True)
def integrate(double low, double high, int npts, **kwargs):
    """Performs numerical integration of the kernel function.
    Parameters
    ----------
    low: float
       Lower limit of the integral
    high: float
       Higher limit of the integral
    npts: int
       Number of points to evaluate the integral over
    **kwargs
       Additional keyword arguments
    """
    cdef double dx = kwargs.get("dx", (high - low) / npts)
    cdef:
        double summ = 0
        int i
    for i in range(npts):
       summ += kernel(low + i*dx)
    return dx * summ
