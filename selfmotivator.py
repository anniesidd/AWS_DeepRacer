"""
"Self Motivating" Reward Function
Reward only if car is on the track, and if it has gone forward.
Reward more if it has gotten farther in fewer steps

Max Speed: 1 m/s
Steering: 30 degrees
Speed Granularity: 3
Sterring Angle Granularity: 3

Training for 30 minutes

"""

def reward_function(params):
    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100)
    else:
        reward = 0.01

    return float(reward)