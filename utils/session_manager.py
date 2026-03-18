sessions = {}

def track_session(user: str):
    if user not in sessions:
        sessions[user] = {"requests": 0}
    
    sessions[user]["requests"] += 1
    return sessions[user]