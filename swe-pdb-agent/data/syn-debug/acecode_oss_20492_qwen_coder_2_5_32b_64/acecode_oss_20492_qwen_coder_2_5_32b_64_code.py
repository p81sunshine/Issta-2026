import time
from collections import defaultdict

# Define rate limits as constants
RATELIMIT_DEFAULT = {'day': 400, 'hour': 100}
RATELIMIT_LIST_THREADS = {'minute': 20, 'second': 1}
RATELIMIT_VIEW_SPECIFIC_POST = {'minute': 20, 'second': 1}
RATELIMIT_NEW_REPLY = {'hour': 20, 'second': 1, 'minute': 2}
RATELIMIT_VIEW_TRIP_META = {'hour': 50, 'minute': 15}
RATELIMIT_EDIT_TRIP_META = {'hour': 60, 'second': 1, 'minute': 4}
RATELIMIT_MANAGE_COOKIE = {'hour': 60, 'second': 1, 'minute': 7}
RATELIMIT_CREATE_THREAD = {'hour': 700, 'minute': 100}
RATELIMIT_NEW_THREAD_FORM = {'hour': 60, 'second': 1}

# Initialize rate limit counters
rate_limit_counters = defaultdict(lambda: defaultdict(list))

# Function to check and update rate limits
def check_rate_limit(action, user_id):
    # Define the rate limits for each action
    rate_limits = {
        'LIST_THREADS': RATELIMIT_LIST_THREADS,
        'VIEW_SPECIFIC_POST': RATELIMIT_VIEW_SPECIFIC_POST,
        'NEW_REPLY': RATELIMIT_NEW_REPLY,
        'VIEW_TRIP_META': RATELIMIT_VIEW_TRIP_META,
        'EDIT_TRIP_META': RATELIMIT_EDIT_TRIP_META,
        'MANAGE_COOKIE': RATELIMIT_MANAGE_COOKIE,
        'CREATE_THREAD': RATELIMIT_CREATE_THREAD,
        'NEW_THREAD_FORM': RATELIMIT_NEW_THREAD_FORM,
        'DEFAULT': RATELIMIT_DEFAULT
    }
    
    # Get the rate limits for the given action or default rate limits
    action_rate_limits = rate_limits.get(action, RATELIMIT_DEFAULT)
    
    # Current time in seconds since epoch
    current_time = time.time()
    
    # Check rate limits for each time frame
    for time_frame, limit in action_rate_limits.items():
        # Calculate the time window for the current time frame
        if time_frame == 'second':
            time_window = 1
        elif time_frame == 'minute':
            time_window = 60
        elif time_frame == 'hour':
            time_window = 3600
        elif time_frame == 'day':
            time_window = 86400
        
        # Remove timestamps that are outside the time window
        rate_limit_counters[action][user_id] = [
            t for t in rate_limit_counters[action][user_id] if current_time - t < time_window
        ]
        
        # Check if the user has exceeded the rate limit for the current time frame
        if len(rate_limit_counters[action][user_id]) >= limit:
            return False
    
    # Add the current timestamp to the rate limit counters
    rate_limit_counters[action][user_id].append(current_time)
    
    # The user is allowed to perform the action
    return True

# Test cases