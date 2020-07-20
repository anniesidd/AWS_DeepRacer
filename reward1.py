"""
First test reward function

Trained for 30m

Hyperparameter Value
Gradient descent batch size	64
Entropy	0.01
Discount factor	0.999
Loss type	Huber
Learning rate	0.0003
Number of experience episodes between each policy-updating iteration	20
Number of epochs	10


RESULTS
Based on graph during training, reward function was not at max when car got farthest around the track
- Should not reward based on speed

Trial  Time  % track completed  Status
1	00:00:01.588	0%	Off track
2	00:00:24.948	89%	Off track
3	00:00:27.426	100%	Lap complete
"""

def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    And reward more when high speed for better track time
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 1.0 * speed * speed

    # Always return a float value
    return float(reward)