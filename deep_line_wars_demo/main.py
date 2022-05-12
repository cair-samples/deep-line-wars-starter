import gym
import deep_line_wars

if __name__ == '__main__':

    # Reset environment
    env = gym.make("deeplinewars-deterministic-11x11-v0", env_config=dict(
        window=True,
        gui=False
    ))
    # env = deep_line_wars.gym_dlw.DeepLineWarsEnvMultiAgentWrapper(env=env)  # Not tested, MA setup.

    num_episodes = 1000
    for episode in range(num_episodes):
        s = env.reset()

        # Set terminal state to false
        terminal = False

        while not terminal:
            # Draw environment on screen
            env.render()  # For image you MUST call this

            # Draw action from distribution
            a = env.action_space.sample()

            # Perform action in environment
            s1, r, t, _ = env.step(a)

            terminal = t

            s = s1
        print(f"Epsisode: {episode} of {num_episodes}")
