#!/usr/bin/env python3
"""
Sample Data Generator
Students: Complete the data generation logic
"""

import sqlite3
import random

def generate_sample_data(db_path, num_participants=20):
    """
    Generate sample survey responses for testing.
    
    Args:
        db_path: Path to SQLite database
        num_participants: Number of sample participants to create
    """
    # TODO: Connect to database
    
    departments = ['IT', 'HR', 'Finance', 'Marketing', 'Operations']
    roles = ['Manager', 'Analyst', 'Specialist', 'Coordinator']
    
    question_categories = {
        'password_unique': 'password_security',
        'password_manager': 'password_security',
        'email_sender_check': 'email_security',
        # TODO: Add more questions
    }
    
    # TODO: Loop to create participants
    # TODO: For each participant:
    #   - Generate random employee data
    #   - Insert participant into database
    #   - Generate responses for each question
    #   - Insert responses into database
    
    print(f"Generated sample data for {num_participants} participants")

if __name__ == "__main__":
    db_path = "../data/assessment.db"
    generate_sample_data(db_path)
