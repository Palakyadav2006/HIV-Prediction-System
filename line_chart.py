import matplotlib.pyplot as plt

def plot_line(data):
    plt.figure()
    trend = data.groupby('Year')['HIV_Prevalence'].mean()
    trend.plot(color='red', marker='o')
    plt.title("Line Chart: HIV Prevalence Over Years")
    plt.xlabel("Year")
    plt.ylabel("HIV Prevalence")
    plt.grid(True)
    plt.show()