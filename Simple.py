# Write a program to determine EOQ using various inventory models.
import math

def basic_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

def eoq_with_shortage(D, S, H, P):
    return math.sqrt((2 * D * S) / H) * math.sqrt((H + P) / P)

def production_eoq(D, S, H, P):
    if P <= D:
        return None
    return math.sqrt((2 * D * S / H) * (P / (P - D)))

print("\n--- EOQ Models ---")
print("1. Basic EOQ")
print("2. EOQ with Shortage")
print("3. Production EOQ")

choice = int(input("Enter your choice: "))

if choice == 1:
    D = float(input("Demand: "))
    S = float(input("Ordering cost: "))
    H = float(input("Holding cost: "))
    print("EOQ =", round(basic_eoq(D, S, H), 2))

elif choice == 2:
    D = float(input("Demand: "))
    S = float(input("Ordering cost: "))
    H = float(input("Holding cost: "))
    P = float(input("Shortage cost: "))
    print("EOQ =", round(eoq_with_shortage(D, S, H, P), 2))

elif choice == 3:
    D = float(input("Demand rate: "))
    S = float(input("Setup cost: "))
    H = float(input("Holding cost: "))
    P = float(input("Production rate: "))
    result = production_eoq(D, S, H, P)
    if result:
        print("EOQ =", round(result, 2))
    else:
        print("Invalid: Production rate must be greater than demand.")

else:
    print("Invalid choice!")


# Write a program to determine different characteristics using various queuing models.

import math

def mm1(lam, mu):
    if lam >= mu:
        print("Unstable system!")
        return
    rho = lam / mu
    Ls = lam / (mu - lam)
    Lq = lam**2 / (mu * (mu - lam))
    Ws = 1 / (mu - lam)
    Wq = lam / (mu * (mu - lam))
    print(f"ρ={rho:.3f}, Ls={Ls:.3f}, Lq={Lq:.3f}, Ws={Ws:.3f}, Wq={Wq:.3f}")

def mm1k(lam, mu, K):
    rho = lam / mu
    P0 = (1 - rho) / (1 - rho**(K+1)) if rho != 1 else 1/(K+1)
    Ls = (rho*(1-(K+1)*rho**K + K*rho**(K+1))) / ((1-rho)*(1-rho**(K+1)))
    lam_eff = lam*(1 - rho**K * P0)
    Lq = Ls - lam_eff/mu
    Ws = Ls / lam_eff
    Wq = Lq / lam_eff
    print(f"P0={P0:.3f}, Ls={Ls:.3f}, Lq={Lq:.3f}, Ws={Ws:.3f}, Wq={Wq:.3f}")

def mmc(lam, mu, c):
    rho = lam/(c*mu)
    if rho >= 1:
        print("Unstable system!")
        return
    sum_part = sum((lam/mu)**n/math.factorial(n) for n in range(c))
    last_part = (lam/mu)**c / (math.factorial(c)*(1-rho))
    P0 = 1/(sum_part + last_part)
    Lq = ((lam/mu)**c * rho / (math.factorial(c)*(1-rho)**2))*P0
    Ls = Lq + lam/mu
    Ws = Ls/lam
    Wq = Lq/lam
    print(f"P0={P0:.3f}, Lq={Lq:.3f}, Ls={Ls:.3f}, Ws={Ws:.3f}, Wq={Wq:.3f}")

print("\n--- QUEUEING MODELS ---")
print("1. M/M/1")
print("2. M/M/1/K")
print("3. M/M/c")

ch = int(input("Enter choice: "))

if ch == 1:
    lam = float(input("Arrival rate λ: "))
    mu = float(input("Service rate μ: "))
    mm1(lam, mu)

elif ch == 2:
    lam = float(input("Arrival rate λ: "))
    mu = float(input("Service rate μ: "))
    K = int(input("System capacity K: "))
    mm1k(lam, mu, K)

elif ch == 3:
    lam = float(input("Arrival rate λ: "))
    mu = float(input("Service rate μ: "))
    c = int(input("Number of servers: "))
    mmc(lam, mu, c)

else:
    print("Invalid choice")


# Write a program to fit Poisson distribution on a given data. 

import math
import matplotlib.pyplot as plt

def poisson_fit_plot(x_values, freq):
    N = sum(freq)

    # Step 1: Mean (λ)
    mean = sum(x * f for x, f in zip(x_values, freq)) / N

    print("\n--- Poisson Distribution Fitting ---")
    print(f"Estimated λ (mean) = {mean:.4f}\n")

    print("x\tObserved\tExpected")

    expected = []
    for x, obs in zip(x_values, freq):
        prob = math.exp(-mean) * (mean ** x) / math.factorial(x)
        exp_freq = N * prob
        expected.append(exp_freq)

        print(f"{x}\t{obs}\t\t{exp_freq:.2f}")

    # -------- Plot --------
    plt.figure()
    plt.plot(x_values, freq, label="Observed")
    plt.plot(x_values, expected, marker='o', linestyle='--', label="Expected (Poisson)")

    plt.xlabel("x")
    plt.ylabel("Frequency")
    plt.title("Poisson Distribution Fit")
    plt.legend()
    plt.grid()
    plt.show()

print("=== POISSON DISTRIBUTION FITTING ===")

n = int(input("Enter number of observations: "))

x_values = []
freq = []

print("\nEnter x values and corresponding frequencies:")

for i in range(n):
    x = int(input(f"x[{i+1}] = "))
    f = int(input(f"f[{i+1}] = "))
    x_values.append(x)
    freq.append(f)

x_values, freq = zip(*sorted(zip(x_values, freq)))

poisson_fit_plot(list(x_values), list(freq))

#Write a program to implement linear regression using python.

import matplotlib.pyplot as plt

def linear_regression(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(x[i]**2 for i in range(n))

    # Slope (b)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

    # Intercept (a)
    a = (sum_y / n) - b * (sum_x / n)

    print("\n--- Linear Regression Result ---")
    print(f"Slope (b) = {b:.4f}")
    print(f"Intercept (a) = {a:.4f}")
    print(f"Regression line: y = {a:.4f} + {b:.4f}x")

    return a, b


def plot_regression(x, y, a, b):
    y_pred = [a + b * xi for xi in x]

    plt.figure()
    plt.scatter(x, y, label="Observed Data")
    plt.plot(x, y_pred, label="Regression Line")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Linear Regression")
    plt.legend()
    plt.grid()
    plt.show()


# -------- Main Program --------
print("=== LINEAR REGRESSION PROGRAM ===")

n = int(input("Enter number of observations: "))

x = []
y = []

print("\nEnter values of X and Y:")

for i in range(n):
    xi = float(input(f"x[{i+1}] = "))
    yi = float(input(f"y[{i+1}] = "))
    x.append(xi)
    y.append(yi)

# Calculate regression
a, b = linear_regression(x, y)

# Plot
plot_regression(x, y, a, b)

'''
x: 1 2 3 4 5  
y: 2 4 5 4 5
'''

# Write a program to fit Binomial distribution on a given data.

import math
import matplotlib.pyplot as plt

def factorial(n):
    return math.factorial(n)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def binomial_fit(x_values, freq, n):
    N = sum(freq)

    # Step 1: Mean
    mean = sum(x * f for x, f in zip(x_values, freq)) / N

    # Step 2: Estimate p
    p = mean / n
    q = 1 - p

    print("\n--- Binomial Distribution Fitting ---")
    print(f"Mean = {mean:.4f}")
    print(f"Estimated p = {p:.4f}, q = {q:.4f}\n")

    print("x\tObserved\tExpected")

    expected = []
    for x, obs in zip(x_values, freq):
        prob = combination(n, x) * (p**x) * (q**(n - x))
        exp_freq = N * prob
        expected.append(exp_freq)

        print(f"{x}\t{obs}\t\t{exp_freq:.2f}")

    # -------- Plot --------
    plt.figure()
    plt.bar(x_values, freq, label="Observed")
    plt.plot(x_values, expected, marker='o', label="Expected (Binomial)")

    plt.xlabel("x")
    plt.ylabel("Frequency")
    plt.title("Binomial Distribution Fit")
    plt.legend()
    plt.grid()
    plt.show()


# -------- Main Program --------
print("=== BINOMIAL DISTRIBUTION FITTING ===")

n_trials = int(input("Enter number of trials (n): "))
m = int(input("Enter number of observations: "))

x_values = []
freq = []

print("\nEnter x values and frequencies:")

for i in range(m):
    x = int(input(f"x[{i+1}] = "))
    f = int(input(f"f[{i+1}] = "))
    x_values.append(x)
    freq.append(f)

# Sort for proper plotting
x_values, freq = zip(*sorted(zip(x_values, freq)))

binomial_fit(list(x_values), list(freq), n_trials)

'''
n = 4
x: 0 1 2 3 4
f: 5 12 18 10 5
'''

# Write a program in python to plot a histogram of a given data set.

import matplotlib.pyplot as plt

# -------- Main Program --------
print("=== HISTOGRAM PROGRAM ===")

# Taking input
data = list(map(float, input("Enter data values (space-separated): ").split()))

# Number of bins (intervals)
bins = int(input("Enter number of bins: "))

# Plot histogram
plt.figure()
plt.hist(data, bins=bins)

plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Histogram of Given Data")
plt.grid()

plt.show()

'''
Enter data values: 10 20 20 30 30 30 40 50 60
Enter number of bins: 5
'''

# Write a program to test the significance of two samples have been drawn from the same Normal population.

from scipy import stats

sample1 = list(map(float, input("Enter sample 1: ").split()))
sample2 = list(map(float, input("Enter sample 2: ").split()))

t_stat, p_value = stats.ttest_ind(sample1, sample2)

print(f"t = {t_stat:.4f}, p-value = {p_value:.4f}")

if p_value < 0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")

'''
Sample 1: 10 12 11 13 12  
Sample 2: 14 15 13 16 15  
'''