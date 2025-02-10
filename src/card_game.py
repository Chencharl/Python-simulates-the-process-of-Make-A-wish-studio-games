def simulate_game(num_cards, character):
    import random
    
    # Simulate drawing cards
    bumps = 1  # Start with one bump for the character
    for _ in range(num_cards):
        if random.random() < 0.1:  # Assuming a 10% chance to bump the character
            bumps += 1
            
    return bumps

def simulate_for_character(character, num_trials, num_cards):
    results = []
    for _ in range(num_trials):
        bumps = simulate_game(num_cards, character)
        results.append(bumps)
        
    return results