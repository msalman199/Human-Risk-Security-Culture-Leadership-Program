#!/usr/bin/env python3
"""
Human Risk Assessment Scoring System
Students: Complete the functions to calculate risk scores
"""

import sqlite3
import pandas as pd

class RiskScorer:
    def __init__(self, db_path):
        self.db_path = db_path
        self.risk_weights = {
            'password_security': 0.25,
            'email_security': 0.20,
            'social_engineering': 0.20,
            'device_security': 0.15,
            'training_awareness': 0.20
        }
    
    def calculate_category_score(self, responses, category):
        """
        Calculate risk score for a specific category.
        
        Args:
            responses: List of response dictionaries
            category: Category name to calculate score for
        
        Returns:
            Score between 0-100
        """
        # TODO: Filter responses by category
        # TODO: Calculate total score from response values
        # TODO: Calculate percentage score (assuming 1-5 scale)
        # TODO: Return normalized score (0-100)
        pass
    
    def calculate_overall_risk(self, category_scores):
        """
        Calculate overall risk score using weighted categories.
        
        Args:
            category_scores: Dictionary of category scores
        
        Returns:
            Weighted overall score
        """
        # TODO: Apply weights to each category score
        # TODO: Sum weighted scores
        # TODO: Return overall risk score
        pass
    
    def get_risk_level(self, score):
        """
        Determine risk level based on score.
        
        Args:
            score: Risk score (0-100)
        
        Returns:
            Risk level string
        """
        # TODO: Implement risk level thresholds
        # 80-100: Low Risk
        # 60-79: Medium Risk
        # 40-59: High Risk
        # 0-39: Critical Risk
        pass
    
    def process_participant_scores(self, participant_id):
        """
        Process and store risk scores for a participant.
        
        Args:
            participant_id: ID of participant to process
        
        Returns:
            Tuple of (category_scores, overall_score)
        """
        # TODO: Connect to database
        # TODO: Retrieve participant responses
        # TODO: Calculate category scores
        # TODO: Calculate overall score
        # TODO: Store scores in database
        # TODO: Return results
        pass

if __name__ == "__main__":
    scorer = RiskScorer("../data/assessment.db")
    print("Risk scoring system initialized")
