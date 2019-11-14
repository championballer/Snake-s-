from gym.envs.registration import register

register(
    id='snakeai-v0',
    entry_point='gym_snakeai.envs:snakeai',
)