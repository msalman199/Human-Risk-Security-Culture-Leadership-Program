import sqlite3
import random
from datetime import datetime, timedelta

def generate_sample_data():
    """
    Generate realistic sample data for testing.
    
    TODO: Generate 100 employees across 6 departments
    TODO: Create 2-6 training records per employee
    TODO: Create 3-8 phishing simulation records per employee
    TODO: Create 50 security incidents
    TODO: Create 1-3 survey responses per employee
    """
    conn = sqlite3.connect('data/security_culture.db')
    cursor = conn.cursor()
    
    departments = ['IT', 'HR', 'Finance', 'Marketing', 'Operations', 'Sales']
    
    # TODO: Generate employee data
    # TODO: Generate training completion data with scores
    # TODO: Generate phishing simulation results
    # TODO: Generate security incident records
    # TODO: Generate survey responses
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    generate_sample_data()
