import gym
from gym import spaces
import numpy as np

class MessageRoutingEnv(gym.Env):
    def __init__(self, num_nodes):
        super(MessageRoutingEnv, self).__init__()
        self.num_nodes = num_nodes
        self.num_actions = self.num_nodes
        self.observation_space = spaces.Discrete(self.num_nodes)
        self.action_space = spaces.Discrete(self.num_actions)
        self.state = None
        self.target_node = None
        self.step_count = 0
        self.episode_paths = []

    def reset(self):
        self.state = np.random.randint(0, self.num_nodes)
        self.target_node = np.random.randint(0, self.num_nodes)
        self.step_count = 0
        self.current_path = [self.state]
        return self.state

    def step(self, action):
        reward = 1 if action == self.target_node else 0
        self.step_count += 1
        self.current_path.append(action)
        done = self.step_count >= 20
        if done:
            self.episode_paths.append(self.current_path)
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
