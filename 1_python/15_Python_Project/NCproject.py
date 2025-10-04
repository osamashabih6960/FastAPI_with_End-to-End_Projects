import streamlit as st
import sympy as sy
import math


def f(x):
    return 1 / (1 + x * x)


def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    k = 1
    sum = 0
    while k < n:
        t = a + k * h
        sum += f(t)
        k += 1
    int_a = (h / 2) * (f(a) + f(b) + 2 * sum)
    return int_a


def exact_value():
    x = sy.Symbol("x")
    int_e = sy.integrate(f(x), (x, 0, 1))
    return float(int_e)


st.title("Trapezoidal Rule Integration")

user_choice = st.radio(
    "Choose input method:",
    ('Use default values', 'Enter custom values')
)

if user_choice == 'Use default values':
    a = 0
    b = 1
    n = 4
else:
    a = st.number_input("Enter lower limit:", value=0.0)
    b = st.number_input("Enter upper limit:", value=1.0)
    n = st.number_input("Enter number of strips:", min_value=1, value=4, step=1)

if st.button("Calculate"):
    int_a = trapezoidal_rule(a, b, n)
    int_e = exact_value()
    error = abs(int_e - int_a)

    st.write(f"The value of integration using the Trapezoidal Rule is: {int_a:.6f}")
    st.write(f"Exact value is: {int_e:.6f}")
    st.write(f"Error: {error:.6f}")

    # Visualize the function and the trapezoidal approximation
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(a, b, 1000)
    y = [f(xi) for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y, 'b-', label='f(x) = 1 / (1 + x^2)')

    # Plot trapezoids
    x_trapezoid = np.linspace(a, b, n + 1)
    y_trapezoid = [f(xi) for xi in x_trapezoid]
    ax.plot(x_trapezoid, y_trapezoid, 'ro-')

    for i in range(n):
        ax.fill_between([x_trapezoid[i], x_trapezoid[i + 1]],
                        [y_trapezoid[i], y_trapezoid[i + 1]],
                        alpha=0.3)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('Trapezoidal Rule Approximation')
    st.pyplot(fig)