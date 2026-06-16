<?php
/**
 * Survey Processing Script
 * Students: Complete the database insertion logic
 */

$db_path = '/home/' . get_current_user() . '/human-risk-assessment/data/assessment.db';

function insertParticipant($db, $employee_id, $department, $role, $experience_years) {
    // TODO: Prepare SQL statement for participant insertion
    // TODO: Bind parameters
    // TODO: Execute statement
    // TODO: Return last insert ID
}

function insertRiskResponse($db, $participant_id, $question_id, $response_value, $category) {
    // TODO: Prepare SQL statement for response insertion
    // TODO: Bind parameters
    // TODO: Execute statement
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
        // TODO: Connect to SQLite database
        // TODO: Insert participant data
        // TODO: Get participant ID
        
        // Define question-to-category mapping
        $question_categories = [
            'password_unique' => 'password_security',
            'password_manager' => 'password_security',
            'email_sender_check' => 'email_security',
            // TODO: Add more mappings
        ];
        
        // TODO: Loop through responses and insert into database
        
        echo "<h1>Thank You!</h1>";
        echo "<p>Your survey response has been recorded.</p>";
        
    } catch (Exception $e) {
        echo "<h1>Error</h1>";
        echo "<p>Error processing survey: " . $e->getMessage() . "</p>";
    }
}
?>
