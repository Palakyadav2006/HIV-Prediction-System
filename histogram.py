import matplotlib.pyplot as plt

def plot_histogram(data):
    plt.figure()
    plt.hist(data['CD4_Count'], bins=20, color='orange')
    plt.title("Histogram: CD4 Count Distribution")
    plt.xlabel("CD4 Count")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()