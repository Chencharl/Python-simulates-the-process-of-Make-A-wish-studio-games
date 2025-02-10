def calculate_probability_distribution(simulation_results):
    """
    Calculate the probability distribution of bumps for each character based on simulation results.
    
    Args:
        simulation_results (dict): A dictionary where keys are character names and values are lists of bumps.
    
    Returns:
        dict: A dictionary with character names as keys and their probability distributions as values.
    """
    probability_distribution = {}
    
    for character, bumps in simulation_results.items():
        total_trials = len(bumps)
        bump_counts = {}
        
        for bump in bumps:
            if bump in bump_counts:
                bump_counts[bump] += 1
            else:
                bump_counts[bump] = 1
        
        probability_distribution[character] = {bump: count / total_trials for bump, count in bump_counts.items()}
    
    return probability_distribution

def main():
    # Example usage
    simulation_results = {
        'Character A': [1, 2, 1, 3, 2],
        'Character B': [2, 2, 3, 1, 1],
    }
    
    probabilities = calculate_probability_distribution(simulation_results)
    print(probabilities)

if __name__ == "__main__":
    main()