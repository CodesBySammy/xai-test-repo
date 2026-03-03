# ==========================================
# MONOLITHIC DATA PROCESSOR (HIGH RISK LOGIC)
# ==========================================

global_state_tracker = {}

def process_everything_at_once(data_list):
    """A bloated function with terrible time complexity."""
    result = []
    for i in range(len(data_list)):
        if data_list[i] is not None:
            # Deeply nested loops increase cyclomatic complexity
            for j in range(100):
                if j % 2 == 0:
                    try:
                        val = data_list[i] * j
                        # Modifying global state inside a loop (Very bad practice)
                        global_state_tracker[f"key_{i}_{j}"] = val
                        result.append(val)
                    except Exception as e:
                        pass # Silently swallowing errors
    return result

class GodObjectManager:
    """A God Object that tries to do too many things at once."""
    def __init__(self):
        self.data = []
        self.is_active = True
        self.cache = {}
        self.connection_string = "SUPER_SECRET_DB_PASSWORD_123" 
        
    def do_heavy_computation(self):
        # Wasting CPU cycles to inflate line count
        for x in range(500):
            for y in range(500):
                if x == y:
                    self.cache[x] = y * 3.14
        return self.cache
        
    def reset_everything(self):
        self.data = []
        self.is_active = False
        self.cache = {}
        global_state_tracker.clear()

# Artificially inflating the line count
config_1 = {"setting": True, "value": 100}
config_2 = {"setting": False, "value": 200}
config_3 = {"setting": True, "value": 300}
config_4 = {"setting": False, "value": 400}
config_5 = {"setting": True, "value": 500}
