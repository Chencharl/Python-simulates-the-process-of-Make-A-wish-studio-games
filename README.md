# Card Game Simulation

This project simulates a card game to calculate the probability of character bumps in a wish live stream. The simulation runs multiple trials to gather data on character bumps and visualizes the results using line graphs.

## Project Structure

```
card-game-simulation
├── src
│   ├── __init__.py
│   ├── card_game.py
│   ├── probability_calculator.py
│   ├── graph_plotter.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

## Usage

1. **Simulate the Game**: Use the `simulate_game` function in `card_game.py` to run the game simulation. You can specify the number of trials and the characters involved.

2. **Calculate Probabilities**: After running the simulations, use the `probability_calculator.py` to analyze the results and calculate the probability distribution of bumps for each character.

3. **Visualize Results**: Finally, use the `graph_plotter.py` to create line graphs that display the probability distribution of bumps for each character.

## Example

Here is a simple example of how to run the simulation:

```python
from src.card_game import simulate_game
from src.probability_calculator import calculate_probabilities
from src.graph_plotter import plot_results

# Simulate the game
results = simulate_game(num_trials=1000)

# Calculate probabilities
probabilities = calculate_probabilities(results)

# Plot the results
plot_results(probabilities)
```

## Interpretation of Results

The line graphs generated will show the probability distribution of bumps for each character. Peaks in the graph indicate characters that are more likely to receive bumps during the wish live stream.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License.