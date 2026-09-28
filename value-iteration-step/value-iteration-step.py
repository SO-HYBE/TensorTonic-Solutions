def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Returns one updated floating-point value for every state.
    """
    # Write code here
    output = []
    
    for state in range(len(transitions)):
        pred_val = []
        for action in range(len(rewards[state])):
            inr_brkt = 0
            for f_state in range(len(values)):
                inr_brkt += ((transitions[state][action][f_state] * values[f_state]))
                
            Q_sa = rewards[state][action] + (gamma * inr_brkt)
            pred_val.append(Q_sa)

        v_max = max(pred_val)
        output.append(v_max)
    return output