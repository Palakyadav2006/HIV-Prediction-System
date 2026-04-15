import matplotlib.pyplot as plt

def plot_box(data):
    plt.figure()
    plt.boxplot(data['CD4_Count'], patch_artist=True,
                boxprops=dict(facecolor='purple'))
    plt.title("Box Plot: CD4 Count Distribution")
    plt.ylabel("CD4 Count")
    plt.grid(True)
    plt.show()