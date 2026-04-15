import matplotlib.pyplot as plt

def plot_bar(data):
    plt.figure()
    data.groupby('Country')['HIV_Prevalence'].mean().head(10).plot(
        kind='bar', color='green'
    )
    plt.title("Bar Chart: Top 10 Countries HIV Prevalence")
    plt.xlabel("Country")
    plt.ylabel("HIV Prevalence")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()