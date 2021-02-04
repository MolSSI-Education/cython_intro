if __name__ == "__main__":
    from timer import timeit

    kwargs = {"low": -5, "high": 5, "npts": 50000}

    # Python
    import pymod

    timep, resultp = timeit(pymod.integrate, iters=200, **kwargs)
    print(f"Python: time = {timep:.4f}s, result = {resultp:.4f}")

    # Cython
    import cymod

    timec, resultc = timeit(cymod.integrate, iters=200, **kwargs)
    print(f"Cython: time = {timec:.4f}s, result = {resultc:.4f}")

    # Relative speedup
    print(f"Cython/python speedup: {timep/timec}")
