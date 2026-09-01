"""
bill.py — the Bill Splitter module.

This is a *module*: a collection of small, reusable functions. None of them read
input or print anything — they just take values in and return a value out. That's
what makes them easy to test (see tests/test_unit.py) and easy to reuse from the
console, notebook, and Streamlit interfaces (console.py, explore.ipynb, dashboard.py).

Your job: implement the four functions below so the Unit Tests in
tests/test_unit.py all pass. Each docstring says exactly what the function should
return — replace the `# TODO` line (and the `pass`) with your code.
"""
def tip_amount(subtotal, pct):
    """Return the tip amount for a subtotal at the given percentage."""
    return round(subtotal * pct / 100, 2)
def grand_total(subtotal, pct):
    """Return the subtotal plus tip for the given percentage."""
    return round(subtotal + tip_amount(subtotal, pct), 2)
def split_evenly(total, people):
    """Return the amount each person should pay when splitting the total evenly."""
    if people == 0:
        raise ValueError("Number of diners cannot be zero.")
    return round(total / people, 2)
def generous(pct):
    """Return True if the tip percentage is generous (20% or higher), False otherwise."""
    if pct < 0:
        raise ValueError("Tip percentage cannot be negative.")
    return pct >= 20
