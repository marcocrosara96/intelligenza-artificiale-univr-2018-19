from envs.obsgrid_env import ObsGrid


class LavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "L"],
                ["L", "W", "L", "P"],
                ["L", "L", "L", "G"]
            ]
        rewards = {"L": -0.04, "S": -0.04, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class VeryBadLavaFloorEnv(ObsGrid):
    """
    The floor is lava... but very bad and dangerous lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "L"],
                ["L", "W", "L", "P"],
                ["L", "L", "L", "G"]
            ]
        rewards = {"L": -5.0, "S": -5.0, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class NiceLavaFloorEnv(ObsGrid):
    """
    The floor is lava but the agent really likes it! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "L"],
                ["L", "W", "L", "P"],
                ["L", "L", "L", "G"]
            ]
        rewards = {"L": 50.0, "S": 50.0, "P": -50.0, "G": 5.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class BiggerLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome. Bigger grid.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "L", "L", "L", "L", "L"],
            ["L", "L", "W", "L", "L", "P"],
            ["L", "P", "W", "L", "L", "W"],
            ["L", "L", "L", "L", "L", "L"],
            ["P", "L", "L", "L", "L", "G"]
        ]
        rewards = {"L": -0.04, "S": -0.04, "P": -10.0, "G": 10.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class HugeLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome. Bigger grid.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L", "P", "L", "L", "L", "L"],
            ["L", "L", "L", "W", "L", "L", "W", "L", "L", "L"],
            ["L", "L", "P", "W", "L", "L", "W", "L", "P", "L"],
            ["L", "L", "L", "W", "L", "L", "W", "L", "L", "L"],
            ["L", "L", "L", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "L", "P", "L", "L", "L", "L", "L", "L", "P"],
            ["L", "L", "L", "L", "L", "P", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
            ["P", "L", "L", "L", "L", "L", "L", "L", "L", "G"]
        ]
        rewards = {"L": -0.04, "S": -0.04, "P": -10.0, "G": 10.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class LavaFloorExam2018Env(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome. Bigger grid.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "L", "L", "L", "L", "L"],
            ["L", "L", "W", "L", "L", "P"],
            ["L", "P", "W", "L", "L", "W"],
            ["L", "L", "L", "L", "L", "L"],
            ["P", "L", "L", "L", "L", "G"]
        ]
        rewards = {"L": -0.04, "S": -0.04, "P": -10.0, "G": 10.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)
        self.RC = self.R.copy()
        self.TC = self.T.copy()

    def sample(self, state, action):
        """
        Returns a new state sampled from the ones that can be reached from ``state`` executing ``action``

        Args:
            state: state from which to execute ``action``
            action: action to execute

        Returns:
            reached state
        """
        return self.np_random.choice(self.staterange, p=self.TC[state, action])

    def step(self, action):
        """
        Performs a step from the current state executing ``action``

        Args:
            action: action to execute

        Returns:
            (observation, reward, done, info)
        """
        if self.done:
            return None
        ns = self.sample(self.currstate, action)
        r = self.RC[self.currstate, action, ns]
        self.currstate = ns
        if self.grid[ns] == "G" or self.grid[ns] == "P":
            self.done = True
            return ns, r, True, None
        return ns, r, False, None
