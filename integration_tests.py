import pytest
from load_balancer_sems import LoadBalancer

@pytest.fixture
def setup_balancer():
    lb = LoadBalancer(threshold=100)
    return lb

def test_zone_add_update(setup_balancer):
    lb = setup_balancer
    lb.update_zone("ZoneA", 80)
    assert lb.zones["ZoneA"] == 80
    lb.update_zone("ZoneA", 120)
    assert lb.zones["ZoneA"] == 120

def test_zone_deletion(setup_balancer):
    lb = setup_balancer
    lb.update_zone("ZoneB", 150)
    lb.delete_zone("ZoneB")
    assert "ZoneB" not in lb.zones

def test_balance_logic(setup_balancer):
    lb = setup_balancer
    lb.update_zone("Z1", 80)
    lb.update_zone("Z2", 120)
    lb.update_zone("Z3", 200)
    lb.balance_load()
    for v in lb.zones.values():
        assert v <= lb.threshold

def test_simulate_data(setup_balancer):
    lb = setup_balancer
    lb.simulate_data()
    assert len(lb.zones) == 5
    for v in lb.zones.values():
        assert 50 <= v <= 200

def test_threshold_update_and_balance(setup_balancer):
    lb = setup_balancer
    lb.update_zone("ZoneX", 250)
    lb.set_threshold(180)
    lb.balance_load()
    assert all(load <= 180 for load in lb.zones.values())
