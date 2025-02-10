import matplotlib.pyplot as plt

def plot_probability_distribution(character_data):
    for character, probabilities in character_data.items():
        plt.plot(probabilities, label=character)

    plt.title('Probability Distribution of Character Bumps')
    plt.xlabel('Number of Bumps')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid()
    plt.show()