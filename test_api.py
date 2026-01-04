import requests
import json

BASE_URL = "http://localhost:5555"

def test_get_heroes():
    """Test GET /heroes"""
    print("Testing GET /heroes...")
    response = requests.get(f"{BASE_URL}/heroes")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_get_hero_by_id():
    """Test GET /heroes/:id"""
    print("Testing GET /heroes/1...")
    response = requests.get(f"{BASE_URL}/heroes/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_get_powers():
    """Test GET /powers"""
    print("Testing GET /powers...")
    response = requests.get(f"{BASE_URL}/powers")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_get_power_by_id():
    """Test GET /powers/:id"""
    print("Testing GET /powers/1...")
    response = requests.get(f"{BASE_URL}/powers/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_create_hero_power():
    """Test POST /hero_powers"""
    print("Testing POST /hero_powers...")
    data = {
        "strength": "Average",
        "power_id": 1,
        "hero_id": 3
    }
    response = requests.post(f"{BASE_URL}/hero_powers", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_update_power():
    """Test PATCH /powers/:id"""
    print("Testing PATCH /powers/1...")
    data = {
        "description": "Valid Updated Description"
    }
    response = requests.patch(f"{BASE_URL}/powers/1", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running API Tests")
    print("=" * 50)
    print()
    
    test_get_heroes()
    test_get_hero_by_id()
    test_get_powers()
    test_get_power_by_id()
    test_create_hero_power()
    test_update_power()
    
    print("=" * 50)
    print("Tests Complete!")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()