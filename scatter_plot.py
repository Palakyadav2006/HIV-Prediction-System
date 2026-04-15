import matplotlib.pyplot as plt

def plot_scatter(data):
    plt.figure()
    plt.scatter(data['CD4_Count'], data['Viral_Load'], color='blue')
    plt.xlabel("CD4 Count")
    plt.ylabel("Viral Load")
    plt.title("Scatter Plot: CD4 Count vs Viral Load")
    plt.grid(True)
    plt.show()