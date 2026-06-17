import sqlite3

def create_database():
    """
    Create SQLite database with tables for security culture metrics.
    
    TODO: Implement the following tables:
    - employees (id, employee_id, department, role, hire_date)
    - security_training (id, employee_id, training_type, completion_date, score)
    - phishing_simulations (id, employee_id, simulation_date, clicked_link, reported_email)
    - security_incidents (id, employee_id, incident_date, incident_type, severity)
    - security_surveys (id, employee_id, survey_date, awareness_score, behavior_score)
    """
    conn = sqlite3.connect('data/security_culture.db')
    cursor = conn.cursor()
    
    # TODO: Create employees table with appropriate fields
    # TODO: Create security_training table with foreign key to employees
    # TODO: Create phishing_simulations table
    # TODO: Create security_incidents table
    # TODO: Create security_surveys table
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
