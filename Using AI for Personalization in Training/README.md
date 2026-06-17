# 🤖 Using AI for Personalization in Training

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![AI](https://img.shields.io/badge/Powered%20by-AI-blueviolet?style=flat-square)

> *Build a complete AI-powered personalized cybersecurity training delivery system — from user profiling to adaptive content and text-to-speech.*

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [⚙️ Task 1 — Set Up the Environment](#️-task-1-set-up-the-development-environment)
- [👤 Task 2 — User Profile Management](#-task-2-implement-user-profile-management)
- [🧠 Task 3 — AI Content Generator](#-task-3-build-ai-content-generator)
- [🔊 Task 4 — Text-to-Speech System](#-task-4-implement-text-to-speech-system)
- [🚀 Task 5 — Complete Training System](#-task-5-build-complete-training-system)
- [🏆 Expected Outcomes](#-expected-outcomes)
- [🐛 Troubleshooting](#-troubleshooting-tips)
- [📌 Key Takeaways](#-key-takeaways)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🤖 Integrate **AI APIs** for generating personalized cybersecurity training content
- 👤 Implement **user profile management** for adaptive learning systems
- 🔊 Create **text-to-speech automation** for accessibility features
- 🏗️ Build a **complete personalized training delivery system**
- 🎯 Apply **personalization strategies** based on learner characteristics

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🐍 Python | Basic programming knowledge |
| 🌐 REST APIs | Understanding of REST APIs and JSON |
| 🐧 Linux | Familiarity with the command line |
| 🔐 Cybersecurity | Basic cybersecurity concepts |
| 💻 Web Technologies | Understanding of HTML and CSS |

---

## 🖥️ Lab Environment

> **Al Nafi** provides pre-configured Linux-based cloud machines with all necessary tools installed.
> Click **Start Lab** to access your environment.
> The system includes **Python 3**, required libraries, and **TTS engines** pre-installed.

---

## ⚙️ Task 1: Set Up the Development Environment

### 📁 Step 1 — Create Project Structure

```bash
mkdir -p ~/ai-training-lab/{src,data,audio,templates,output}
cd ~/ai-training-lab
python3 -m venv venv
source venv/bin/activate
```

### 📦 Step 2 — Install Required Packages

```bash
pip install openai python-dotenv flask pyttsx3 gtts
```

### 🔑 Step 3 — Configure API Settings

Create `.env` file:

```bash
nano .env
```

Add configuration (use demo mode for this lab):

```env
OPENAI_API_KEY=demo_key
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=1500
TEMPERATURE=0.7
```

---

## 👤 Task 2: Implement User Profile Management

### 📝 Step 1 — Create User Profile Manager

Create `src/user_profile.py`:

```python
import json
import os
from datetime import datetime

class UserProfileManager:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.profiles_file = os.path.join(data_dir, "profiles.json")
        os.makedirs(data_dir, exist_ok=True)

    def create_profile(self, user_id, name, experience_level, learning_style, interests):
        """
        Create a new user profile with personalization attributes.

        Args:
            user_id:          Unique identifier
            name:             User's name
            experience_level: beginner, intermediate, or advanced
            learning_style:   visual, auditory, kinesthetic, or reading
            interests:        List of cybersecurity topics

        Returns:
            Created profile dictionary
        """
        # TODO: Create profile dictionary with all attributes
        # TODO: Add timestamps (created_at, last_updated)
        # TODO: Initialize empty completed_modules list
        # TODO: Save profile using save_profiles()
        # TODO: Return the created profile
        pass

    def load_profiles(self):
        """Load all profiles from JSON file."""
        # TODO: Check if file exists
        # TODO: Read and parse JSON
        # TODO: Return profiles dictionary or empty dict
        pass

    def save_profiles(self, profiles):
        """Save profiles to JSON file."""
        # TODO: Write profiles dictionary to JSON file with indent=2
        pass

    def get_profile(self, user_id):
        """Retrieve specific user profile."""
        # TODO: Load profiles
        # TODO: Return profile for user_id or None
        pass

    def update_profile(self, user_id, updates):
        """Update existing profile with new data."""
        # TODO: Load profiles
        # TODO: Update profile if exists
        # TODO: Update last_updated timestamp
        # TODO: Save and return updated profile
        pass
```

### 🧪 Step 2 — Test Profile Management

Create `test_profiles.py`:

```python
from src.user_profile import UserProfileManager

def test_profile_system():
    """Test the profile management system."""
    manager = UserProfileManager()

    # TODO: Create test profiles for different user types
    # TODO: Test profile retrieval
    # TODO: Test profile updates
    # TODO: Print results to verify functionality
    pass

if __name__ == "__main__":
    test_profile_system()
```

Run the test:

```bash
python test_profiles.py
```

---

## 🧠 Task 3: Build AI Content Generator

### 🤖 Step 1 — Create Content Generator Class

Create `src/content_generator.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

class AIContentGenerator:
    def __init__(self):
        self.api_key  = os.getenv('OPENAI_API_KEY', 'demo_key')
        self.demo_mode = (self.api_key == 'demo_key')

    def generate_personalized_content(self, user_profile, topic):
        """
        Generate personalized training content based on user profile.

        Args:
            user_profile: User profile dictionary
            topic:        Training topic (e.g., 'phishing', 'password_security')

        Returns:
            Personalized lesson content as string
        """
        if self.demo_mode:
            return self._generate_demo_content(user_profile, topic)
        else:
            # TODO: Create personalized prompt using user attributes
            # TODO: Call OpenAI API with the prompt
            # TODO: Return generated content
            pass

    def _generate_demo_content(self, user_profile, topic):
        """Generate demo content for lab purposes."""
        experience     = user_profile.get('experience_level', 'beginner')
        name           = user_profile.get('name', 'Student')
        learning_style = user_profile.get('learning_style', 'visual')

        # TODO: Create content templates for different experience levels
        # TODO: Customize content based on learning style
        # TODO: Include user's name for personalization
        # TODO: Return formatted lesson content

        # Example template structure:
        content = f"""
# {topic.replace('_', ' ').title()} Training for {name}

## Introduction
[Personalized introduction based on experience level]

## Key Concepts
[Adapted to {experience} level]

## Practical Examples
[Tailored to {learning_style} learning style]

## Action Items
[Specific to user's role and interests]
"""
        return content

    def generate_quiz(self, user_profile, topic, num_questions=5):
        """
        Generate personalized quiz questions.

        Args:
            user_profile:  User profile dictionary
            topic:         Quiz topic
            num_questions: Number of questions to generate

        Returns:
            List of question dictionaries
        """
        # TODO: Create questions based on experience level
        # TODO: Adjust difficulty appropriately
        # TODO: Return list of question objects with:
        #       - question text
        #       - options list
        #       - correct answer index
        #       - explanation
        pass
```

### 🗂️ Step 2 — Create Training Manager

Create `src/training_manager.py`:

```python
import json
import os
from datetime import datetime
from src.user_profile import UserProfileManager
from src.content_generator import AIContentGenerator

class TrainingManager:
    def __init__(self):
        self.profile_manager   = UserProfileManager()
        self.content_generator = AIContentGenerator()
        self.sessions_file     = "data/training_sessions.json"

    def create_personalized_lesson(self, user_id, topic):
        """
        Create complete personalized lesson for user.

        Args:
            user_id: User identifier
            topic:   Lesson topic

        Returns:
            Lesson dictionary with content and quiz
        """
        # TODO: Get user profile
        # TODO: Generate personalized content
        # TODO: Generate quiz questions
        # TODO: Create lesson structure with metadata
        # TODO: Save lesson to file
        # TODO: Return complete lesson object
        pass

    def generate_learning_path(self, user_id):
        """
        Generate personalized learning path based on user profile.

        Args:
            user_id: User identifier

        Returns:
            Ordered list of recommended topics
        """
        # TODO: Get user profile
        # TODO: Define topic sequences for each experience level
        # TODO: Prioritize based on user interests
        # TODO: Return customized learning path
        pass

    def save_lesson(self, lesson):
        """Save lesson to persistent storage."""
        # TODO: Load existing sessions
        # TODO: Add new lesson
        # TODO: Write to JSON file
        pass

    def get_user_progress(self, user_id):
        """Get user's training progress and statistics."""
        # TODO: Load all sessions
        # TODO: Filter by user_id
        # TODO: Calculate completion statistics
        # TODO: Return progress summary
        pass
```

### 🧪 Step 3 — Test Content Generation

Create `test_content.py`:

```python
from src.training_manager import TrainingManager

def test_content_generation():
    """Test personalized content generation."""
    manager = TrainingManager()

    # TODO: Create test user profile
    # TODO: Generate lesson for specific topic
    # TODO: Print lesson content
    # TODO: Generate learning path
    # TODO: Display results
    pass

if __name__ == "__main__":
    test_content_generation()
```

---

## 🔊 Task 4: Implement Text-to-Speech System

### 🎙️ Step 1 — Create TTS Engine

Create `src/tts_engine.py`:

```python
import os
import re
import pyttsx3
from gtts import gTTS

class TTSEngine:
    def __init__(self, output_dir="audio"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

        # TODO: Initialize pyttsx3 engine
        # TODO: Configure voice properties (rate, volume)
        pass

    def text_to_speech_offline(self, text, filename):
        """
        Convert text to speech using offline engine (pyttsx3).

        Args:
            text:     Text content to convert
            filename: Output filename (without extension)

        Returns:
            Path to generated audio file
        """
        # TODO: Clean text for TTS
        # TODO: Generate audio file
        # TODO: Save to output directory
        # TODO: Return file path
        pass

    def text_to_speech_online(self, text, filename, lang='en'):
        """
        Convert text to speech using Google TTS (requires internet).

        Args:
            text:     Text content to convert
            filename: Output filename
            lang:     Language code

        Returns:
            Path to generated audio file
        """
        # TODO: Clean text for TTS
        # TODO: Create gTTS object
        # TODO: Save audio file
        # TODO: Return file path
        pass

    def clean_text_for_tts(self, text):
        """
        Remove markdown formatting and clean text for TTS.

        Args:
            text: Raw text with markdown

        Returns:
            Cleaned text suitable for TTS
        """
        # TODO: Remove markdown headers (# ## ###)
        # TODO: Remove bold/italic markers (* **)
        # TODO: Remove code blocks (```)
        # TODO: Remove bullet points and numbering
        # TODO: Clean extra whitespace
        # TODO: Return cleaned text
        pass

    def create_lesson_audio(self, lesson_content, lesson_id, engine='offline'):
        """
        Create audio version of entire lesson.

        Args:
            lesson_content: Full lesson text
            lesson_id:      Unique lesson identifier
            engine:         'offline' or 'online'

        Returns:
            Path to audio file
        """
        # TODO: Clean lesson content
        # TODO: Choose appropriate TTS engine
        # TODO: Generate audio
        # TODO: Return file path
        pass
```

### 🗃️ Step 2 — Create Audio Manager

Create `src/audio_manager.py`:

```python
import json
import os
from datetime import datetime
from src.tts_engine import TTSEngine

class AudioManager:
    def __init__(self):
        self.tts_engine    = TTSEngine()
        self.metadata_file = "data/audio_metadata.json"

    def create_lesson_audio(self, lesson_id, lesson_content, preferences=None):
        """
        Create audio version with metadata tracking.

        Args:
            lesson_id:      Lesson identifier
            lesson_content: Text content
            preferences:    User audio preferences (engine, speed, voice)

        Returns:
            Audio metadata dictionary
        """
        # TODO: Extract preferences or use defaults
        # TODO: Split content into sections if needed
        # TODO: Generate audio for each section
        # TODO: Create metadata object
        # TODO: Save metadata
        # TODO: Return audio information
        pass

    def split_content_into_sections(self, content):
        """
        Split long content into manageable audio sections.

        Args:
            content: Full lesson content

        Returns:
            List of section dictionaries with title and content
        """
        # TODO: Split by markdown headers
        # TODO: Create section objects
        # TODO: Return list of sections
        pass

    def get_audio_metadata(self, lesson_id):
        """Retrieve audio metadata for a lesson."""
        # TODO: Load metadata file
        # TODO: Return metadata for lesson_id
        pass

    def estimate_duration(self, text):
        """Estimate audio duration based on text length."""
        # TODO: Calculate based on average speaking rate
        # TODO: Return duration in seconds
        pass
```

### 🧪 Step 3 — Test TTS System

Create `test_tts.py`:

```python
from src.audio_manager   import AudioManager
from src.training_manager import TrainingManager

def test_tts_system():
    """Test text-to-speech functionality."""
    # TODO: Create sample lesson
    # TODO: Generate audio version
    # TODO: Verify audio file creation
    # TODO: Print metadata
    pass

if __name__ == "__main__":
    test_tts_system()
```

---

## 🚀 Task 5: Build Complete Training System

### 🏗️ Step 1 — Create Main Application

Create `main.py`:

```python
from src.user_profile    import UserProfileManager
from src.training_manager import TrainingManager
from src.audio_manager   import AudioManager

class PersonalizedTrainingSystem:
    def __init__(self):
        self.profile_manager  = UserProfileManager()
        self.training_manager = TrainingManager()
        self.audio_manager    = AudioManager()

    def onboard_user(self, user_id, name, experience, learning_style, interests):
        """
        Onboard new user and create profile.

        Args:
            user_id:        Unique identifier
            name:           User's name
            experience:     Experience level
            learning_style: Preferred learning style
            interests:      List of topics of interest

        Returns:
            Created profile and recommended learning path
        """
        # TODO: Create user profile
        # TODO: Generate personalized learning path
        # TODO: Return onboarding package
        pass

    def deliver_lesson(self, user_id, topic, include_audio=True):
        """
        Deliver complete personalized lesson with optional audio.

        Args:
            user_id:       User identifier
            topic:         Lesson topic
            include_audio: Whether to generate audio version

        Returns:
            Complete lesson package
        """
        # TODO: Generate personalized lesson
        # TODO: Create audio version if requested
        # TODO: Package all materials
        # TODO: Return lesson bundle
        pass

    def track_progress(self, user_id, lesson_id, quiz_score):
        """
        Track user progress and update profile.

        Args:
            user_id:    User identifier
            lesson_id:  Completed lesson
            quiz_score: Quiz performance score
        """
        # TODO: Update user profile with completion
        # TODO: Record quiz score
        # TODO: Update learning path if needed
        pass

    def generate_report(self, user_id):
        """
        Generate progress report for user.

        Args:
            user_id: User identifier

        Returns:
            Progress report dictionary
        """
        # TODO: Get user profile
        # TODO: Calculate statistics
        # TODO: Generate recommendations
        # TODO: Return comprehensive report
        pass
```

### 🎮 Step 2 — Create Interactive Demo

Create `demo.py`:

```python
from main import PersonalizedTrainingSystem

def run_demo():
    """Run interactive demonstration of the system."""
    system = PersonalizedTrainingSystem()

    print("=== Personalized Training System Demo ===\n")

    # TODO: Create sample users with different profiles
    # TODO: Generate personalized lessons for each
    # TODO: Create audio versions
    # TODO: Display results and comparisons
    # TODO: Show how content adapts to different users

    print("\nDemo completed!")

if __name__ == "__main__":
    run_demo()
```

### ▶️ Step 3 — Run Complete System

```bash
python demo.py
```

---

## 🏆 Expected Outcomes

After completing this lab, you should have:

| ✅ Deliverable | Description |
|---|---|
| 👤 Profile System | Functional user profile management system |
| 🤖 Content Engine | AI-powered content personalization engine |
| 🔊 TTS Capability | Text-to-speech audio generation capability |
| 🏗️ Training System | Complete training delivery system |
| 🧠 Adaptive Learning | Understanding of adaptive learning principles |
| 🎮 Working Demo | Working demo with multiple user scenarios |

Verify your implementation:

```bash
# Check created files
ls -la data/
ls -la audio/

# Verify profiles exist
cat data/profiles.json

# Check audio files were generated
ls -la audio/*.mp3
```

---

## 🐛 Troubleshooting Tips

### ⚠️ Issue: TTS Engine Not Working

> **Solution:** Verify pyttsx3 installation and system audio libraries.

```bash
pip install --upgrade pyttsx3
# Try alternative engine (gTTS) if offline engine fails
```

### ⚠️ Issue: Profile Not Saving

> **Solution:** Ensure the data directory has correct permissions.

```bash
chmod 755 data/
# Verify JSON syntax in profile data
# Check disk space availability
```

### ⚠️ Issue: Content Generation Returns Empty

> **Solution:** Verify demo mode and user profile completeness.

```bash
# Check your .env file
cat .env
# Ensure OPENAI_API_KEY=demo_key is set
# Verify user profile has all required fields
# Ensure topic name matches template keys
```

---

## 📌 Key Takeaways

```
╔══════════════════════════════════════════════════════════════╗
║                     KEY TAKEAWAYS                           ║
╠══════════════════════════════════════════════════════════════╣
║  👤  User profiles drive content personalization            ║
║  🤖  AI APIs can generate adaptive educational content      ║
║  🔊  TTS improves accessibility and engagement              ║
║  🧩  Modular design enables system scalability              ║
║  📈  Continue with: analytics, difficulty adjustment,       ║
║      or multi-language support                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📚 Conclusion

This lab demonstrated building a complete **AI-powered personalized training system**. You implemented:

- 👤 **User profiling** for adaptive learning
- 🤖 **AI content generation** that adapts to individual learner needs
- ♿ **Accessibility features** through text-to-speech

These techniques enable creating scalable, customized cybersecurity training that adapts to each learner's level, style, and goals.

---

<div align="center">

![Python](https://img.shields.io/badge/Built%20with-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Al Nafi](https://img.shields.io/badge/Lab-Al%20Nafi-orange?style=for-the-badge)

*Happy Learning! 🚀*

</div>
