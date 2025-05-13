import numpy as np
import gym

# Criação do ambiente
env = gym.make("FrozenLake-v1", is_slippery=True)

# Inicialização da Q-Table
state_size = env.observation_space.n
action_size = env.action_space.n
q_table = np.zeros((state_size, action_size))

# Hiperparâmetros
learning_rate = 0.8
discount_factor = 0.95
episodes = 10000
max_steps = 100
exploration_rate = 1.0
max_exploration_rate = 1.0
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

# Treinamento do agente
for episode in range(episodes):
    state = env.reset()[0]
    done = False

    for step in range(max_steps):
        # Escolha da ação (Exploração vs Exploração)
        if np.random.uniform(0, 1) < exploration_rate:
            action = env.action_space.sample()  # Exploração
        else:
            action = np.argmax(q_table[state, :])  # Exploração

        # Realiza a ação e observa o resultado
        new_state, reward, done, _, _ = env.step(action)

        # Atualização da Q-Table
        q_table[state, action] = q_table[state, action] + learning_rate * (
            reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action]
        )

        state = new_state

        if done:
            break

    # Decaimento da taxa de exploração
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(
        -exploration_decay_rate * episode
    )

# Teste do agente treinado
state = env.reset()[0]
env.render()
done = False

print("\nAgente treinado jogando:")
for step in range(max_steps):
    action = np.argmax(q_table[state, :])
    new_state, reward, done, _, _ = env.step(action)
    env.render()
    state = new_state
    if done:
        break

env.close()