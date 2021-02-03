if __name__ == "__main__":
    from timer import timeit

    kwargs = {"low": -5, "high": 5, "Npts": 50000}

    # Python
    import pymod

    time, result = timeit(pymod.integrate, iters=100, **kwargs)
    print(f"Python: time = {time:.4f}, result = {result:.4f}")

    # Cython
    import cymod

    time, result = timeit(cymod.integrate, iters=100, **kwargs)
    print(f"Cython: time = {time:.4f}, result = {result:.4f}")
