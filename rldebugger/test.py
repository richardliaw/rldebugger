import gym
import numpy as np

from envs import create_env

env = create_env("Pong-v4")
state = env.reset()

import matplotlib.pyplot as plt
from collections import defaultdict

def rollout(env):
    s = env.reset()
    done = False
    result = defaultdict(list)
    while not done:
        action = env.action_space.sample()
        result["s"].append(s.reshape(42, 42))
        result["a"].append(action)
        s, r, done, _ = env.step(action)
        result["r"].append(r)
    return result

results = rollout(env)

# get_ipython().magic('load_ext autoreload')
# get_ipython().magic('autoreload 2')
from animations import gif

states = np.array(results['s']) * 255
# states shape shape should be (num_states, r, c, channels)
gif("test.gif", states )
