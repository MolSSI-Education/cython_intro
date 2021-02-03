import math


def kernel(x, width=2):
    """Returns the nornalized value of a Gaussian-like function.
    Parameters
    ----------
    x: float
       x-cartesian coordinate
    width: float, optional
       width of the distribution
    """
    normk = 2.0 / (width * math.sqrt(width * math.pi))
    return normk * x**2 * math.exp(-(x ** 2) / width)


def integrate(low, high, Npts, **kwargs):
    """Performs numerical integration of the kernel function.
    Parameters
    ----------
    low: float
       Lower limit of the integral
    high: float
       Higher limit of the integral
    Npts: int
       Number of points to evaluate the integral over
    **kwargs
       Additional keyword arguments
    """
    dx = kwargs.get("dx") or (high - low) / Npts
    return dx * sum([kernel(low + i * dx) for i in range(Npts)])
