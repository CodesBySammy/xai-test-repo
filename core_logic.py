# ==========================================
# REFACTORED DATA PROCESSOR (CLEAN LOGIC)
# ==========================================

def process_data_clean(data_list):
    """A clean, refactored function with O(N) time complexity."""
    if not data_list:
        return []
        
    # Using a simple list comprehension instead of nested loops
    return [val * 2 for val in data_list if val is not None]

class CleanDataManager:
    """A focused class that only does one thing."""
    def __init__(self):
        self.cache = {}
        
    def add_to_cache(self, key, value):
        self.cache[key] = value
        
    def clear_cache(self):
        self.cache.clear()
