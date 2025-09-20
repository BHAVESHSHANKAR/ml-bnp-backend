#!/usr/bin/env python3
"""
Test script to verify the risk calculation fix
"""

import requests
import json

def test_risk_calculation():
    """Test the risk calculation with the provided data"""
    
    # Your test data
    risk_scores = [55, 0, 55, 100, 0, 30, 0, 30, 30, 30, 55]
    expected_average = sum(risk_scores) / len(risk_scores)
    
    print("🧪 Testing Risk Calculation Fix")
    print("=" * 50)
    print(f"📊 Input Risk Scores: {risk_scores}")
    print(f"📊 Expected Average: {expected_average:.2f}")
    print()
    
    # Test with simple average (should give ~35)
    try:
        response = requests.post('http://127.0.0.1:5001/test-risk-calculation', 
                               json={
                                   'risk_scores': risk_scores,
                                   'simple_average': True
                               })
        
        if response.status_code == 200:
            data = response.json()
            result = data['data']['calculated_result']
            calculated_score = result['overall_risk_score']
            
            print("✅ Simple Average Test:")
            print(f"   Expected: {expected_average:.2f}")
            print(f"   Calculated: {calculated_score}")
            print(f"   Difference: {abs(calculated_score - expected_average):.2f}")
            print(f"   Status: {result['overall_status']}")
            print(f"   Category: {result['risk_category']}")
            
            if abs(calculated_score - expected_average) < 1.0:
                print("   ✅ PASS - Risk calculation is now correct!")
            else:
                print("   ❌ FAIL - Risk calculation still has issues")
        else:
            print(f"❌ API Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the ML backend server is running on port 5001")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print()
    
    # Test with adjustments (should be close to 35 + small adjustments)
    try:
        response = requests.post('http://127.0.0.1:5001/test-risk-calculation', 
                               json={
                                   'risk_scores': risk_scores,
                                   'simple_average': False
                               })
        
        if response.status_code == 200:
            data = response.json()
            result = data['data']['calculated_result']
            calculated_score = result['overall_risk_score']
            
            print("🔧 With Adjustments Test:")
            print(f"   Base Average: {expected_average:.2f}")
            print(f"   Final Score: {calculated_score}")
            print(f"   Adjustments: {calculated_score - expected_average:.2f}")
            print(f"   Status: {result['overall_status']}")
            print(f"   Category: {result['risk_category']}")
            
            if calculated_score < 100 and calculated_score > 20:
                print("   ✅ PASS - Adjustments are reasonable")
            else:
                print("   ⚠️  WARNING - Adjustments might be too high")
                
        else:
            print(f"❌ API Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_risk_calculation()
