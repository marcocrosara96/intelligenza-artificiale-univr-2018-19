import numpy as np
from gym.envs.toy_text.cliffwalking import CliffWalkingEnv


class CliffWalkingExam2018Env(CliffWalkingEnv):
    """
    Extension of the CliffWalking environment to make it compatible with the intreface of the lab sessions
    """
    def __init__(self):
        super().__init__()
        self.startstate = np.ravel_multi_index((3, 0), self.shape)
        self.goalstate = np.ravel_multi_index((3, 11), self.shape)
        self.actions = {0: "U", 1: "R", 2: "D", 3: "L"}

    def sample(self, s, a):
        return self.P[s][a][0][1]

    def state_to_pos(self, s):
        return divmod(s, self.shape[1])

    def pos_to_state(self, x, y):
        return x * self.shape[1] + y
