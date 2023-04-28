import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define functions for Trapezoidal rule, Simpson's 1/3rd rule, and Simpson's 3/8th rule
def trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    integral = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])
    return integral

def simpsons_one_third(f, a, b, n):
    if n % 2 != 0:
        st.warning("n must be even (a multiple of 2) for Simpson's 1/3rd Rule")
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    integral = (h/3) * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[n])
    return integral

def simpsons_three_eighth(f, a, b, n):
    if n % 3 != 0:
        st.warning("n must be a multiple of 3 for Simpson's 3/8th Rule")
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    integral = (3*h/8) * (y[0] + 3*np.sum(y[1:n-1:3]) + 3*np.sum(y[2:n:3]) + 2*np.sum(y[3:n-2:3])  + y[n])
    return integral

# Trapezoidal rule equation
trapezoidal_eq = r'''
    \int_{a}^{b} f(x) dx \approx \frac{b-a}{2n}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right]
    '''

# Simpson's 1/3 rule equation
simpsons_one_third_eq = r'''
    \int_{a}^{b} f(x) dx \approx \frac{b-a}{3n}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)\right]
    '''

# Simpson's 3/8 rule equation
simpsons_three_eighth_eq = r'''
    \int_{a}^{b} f(x) dx \approx 3\frac{b-a}{8n}\left[f\left(x_0\right)+3 f\left(x_1\right)+3 f\left(x_2\right)+2 f\left(x_3\right)+3 f\left(x_4\right)+3 f\left(x_5\right)+2 f\left(x_6\right)+\cdots+2 f\left(x_{n-3}\right)+3 f\left(x_{n-2}\right)+3 f\left(x_{n-1}\right)+f\left(x_n\right)\right]
    '''


# Define the function to be integrated
def f(x):
    return eval(input_function)

st.set_page_config(page_title="Numerical Integration Techniques", page_icon=":pencil:", layout="wide")

# Sidebar
st.sidebar.markdown("# About the Author")
st.sidebar.markdown("Created by Manas Sharma (Phys Whiz)")
st.sidebar.markdown("[Personal Website](https://manas.bragitoff.com)")
st.sidebar.markdown("[YouTube Channel](https://youtube.com/@PhysWhiz)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/___physwhiz___/)")
st.sidebar.markdown("[Blog](https://bragitoff.com)")
st.sidebar.markdown("[Twitter](https://twitter.com/ManasSharma07)")

# Main Page
st.title("Numerical Integration Techniques")
st.markdown("## Demonstration via Python and visualization")

# Define the input space
st.write("Enter the function to be integrated in Python syntax (numpy and math functions are allowed)")
input_function = st.text_input("f(x)", "np.sin(x)")

a = st.number_input(label="Lower Limit", value=0.0)
b = st.number_input(label="Upper Limit", value=2*np.pi)

st.subheader("Adjust the number of subintervals (Should be odd for Simpson's 3/8th Rule):")
n = st.number_input("Number of subintervals", value=3, max_value=1000, step=1)




# Plot the function and highlight the area under the curve according to the limits entered
x = np.linspace(a, b, n+1)
y = f(x)
x_actual_func = np.linspace(a, b, 500)
y_actual_func = f(x_actual_func)
fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=2, label='Trapezoidal Rule Approximation')
ax.plot(x_actual_func, y_actual_func, color='brown', linestyle='dashed', linewidth=0.7, label='Actual Function')
ax.fill_between(x, y, where=(x>=a)&(x<=b), color='grey', alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Area under the curve')
ax.legend(loc='upper right')

# Plot the sub-intervals
for i in range(n):
    ax.axvline(x[i], color='r', linestyle='--', linewidth=0.5)

# Display the equations using st.latex
st.write('### Formula:')
st.write('#### Trapezoidal Rule')
st.latex(trapezoidal_eq)
st.write('#### Simpsons 1/3rd Rule')
st.latex(simpsons_one_third_eq)
st.write('#### Simpsons 3/8th Rule')
st.latex(simpsons_three_eighth_eq)


# Calculate the integrals using the three methods
# Display the results
st.write('### Results:')
if n<=1:
    st.error('The no.of sub-intervals cannot be smaller than 2!')
else:
    st.success("Trapezoidal rule: " + str(trapezoidal(f, a, b, n)))
    if n%2!=0:
        st.warning('The no.of sub-intervals is odd, therefore we cannot use the Simpsons 1/3rd formula')
    if n%3==0:
        st.success("Simpson's 3/8th rule: " + str(simpsons_three_eighth(f, a, b, n)))
    if n%3!=0:
        st.warning('The no.of sub-intervals is not a multiple of 3, therefore we cannot use the Simpsons 3/8th formula.')
    if n%2==0:
        st.success("Simpson's 1/3rd rule: " + str(simpsons_one_third(f, a, b, n)))


st.write('### Visualization:')
# Show the plot
st.pyplot(fig)
