import gym
import numpy as np

class MessageRoutingEnv(gym.Env):
    def __init__(self):
        super(MessageRoutingEnv, self).__init__()
        self.num_nodes = 10  # Number of nodes in the network
        self.num_actions = self.num_nodes  # Actions represent selecting a node for routing
        self.observation_space = spaces.Discrete(self.num_nodes)
        self.action_space = spaces.Discrete(self.num_actions)
        self.state = None  # Current state (node)
        self.target_node = None  # Target node for routing
        self.step_count = 0  # Number of steps taken in the episode

    def reset(self):
        # Initialize the environment at the start of each episode
        self.state = np.random.randint(0, self.num_nodes)
        self.target_node = np.random.randint(0, self.num_nodes)
        self.step_count = 0
        return self.state

    def step(self, action):
        # Define the routing logic, compute the reward, and update the state
        # This is where you implement the core routing algorithm
        reward = 1 if action == self.target_node else 0  # Reward for reaching the target node
        self.step_count += 1
        done = self.step_count >= 20  # End episode after a certain number of steps
        return self.state, reward, done, {}

    def render(self):
        pass

    def close(self):
        pass

class QLearningAgent:
    def __init__(self, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.3):
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.q_table = np.zeros((num_actions, num_actions))

    def select_action(self, state):
        if np.random.uniform(0, 1) < self.exploration_prob:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.discount_factor * np.max(self.q_table[next_state, :])
        self.q_table[state, action] += self.learning_rate * (target - predict)

        
def train_agent(env, agent, total_episodes=1000):
    for episode in range(total_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update_q_table(state, action, reward, next_state)
            state = next_state
            total_reward += reward

            if done:
                break

        print(f"Training Episode: {episode}, Total Reward: {total_reward}")

    # Save the trained Q-table (optional)
    np.save("q_table.npy", agent.q_table)

def test_agent(env, agent, total_episodes=100):
    # Load the trained Q-table (optional)
    agent.q_table = np.load("q_table.npy")

    for episode in range(total_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)
            state = next_state
            total_reward += reward

            if done:
                break

        print(f"Test Episode: {episode}, Total Reward: {total_reward}")

def main():
    # Create the environment
    env = MessageRoutingEnv()

    # Create the Q-learning agent
    agent = QLearningAgent(env.num_actions)

    # Train the agent
    train_agent(env, agent, total_episodes=1000)

    # Test the agent
    test_agent(env, agent, total_episodes=100)

    # Close the environment
    env.close()

if __name__ == "__main__":
    main()
