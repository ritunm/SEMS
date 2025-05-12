# profile_balance.py
import os
import cProfile
import pstats
from load_balancer_sems import LoadBalancer

def run_profile():
    lb = LoadBalancer(threshold=100)
    lb.simulate_data()
    lb.balance_load()

if __name__ == "__main__":
    os.makedirs("test_report", exist_ok=True)  # Ensure directory exists
    profiler = cProfile.Profile()
    profiler.enable()
    run_profile()
    profiler.disable()
    profiler.dump_stats("test_report/balance_profile.prof")
    
    stats = pstats.Stats(profiler)
    stats.sort_stats("cumtime").print_stats(10)
