<<<<<<< HEAD
=======

>>>>>>> e35e7c2 (Initial commit)
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

<<<<<<< HEAD
# Resolve project id with fallbacks so the app can load without ADC
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
if not project_id:
    try:
        _, project_id = google.auth.default()
    except Exception:
        project_id = "qwiklabs-gcp-03-dddd65c1188e"

os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
=======
from vertexai.preview.generative_models import GenerativeModel
import json

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id) # project_id
>>>>>>> e35e7c2 (Initial commit)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


<<<<<<< HEAD
def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
=======
def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from a PDF or image file using GCP Vision API or PDF parser.

    Args:
        file_path: Path to the uploaded file in Cloud Storage.

    Returns:
        Extracted text as a string.
    """
    # TODO: Integrate with Vision API for images, PDF parser for PDFs
    return "Extracted lesson text from file."


def extract_key_concepts(lesson_text: str) -> list:
    """
    Uses Vertex AI LLM to extract key concepts from lesson text.

    Args:
        lesson_text: The full lesson text.

    Returns:
        List of key concepts.
    """
    # TODO: Call Vertex AI LLM for summarization/key concept extraction
    return ["Concept 1", "Concept 2"]


def generate_quiz(lesson_text: str) -> list:
    """
    Generates quiz questions from lesson text using Vertex AI.

    Args:
        lesson_text: The full lesson text.

    Returns:
        List of quiz questions (dicts with question, options, answer).
    """
    # Use Vertex AI Gemini API to generate quiz questions
    prompt = f"""
    You are an educational assistant. Given the following lesson text, generate 3 multiple-choice questions with 4 options each and indicate the correct answer.

    Lesson:
    {lesson_text}

    Format:
    [
        {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "A"}},
        ...
    ]
    Return only valid JSON.
    """
    try:
        model = GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        # The model's response should be a JSON array of questions
        # Try to extract JSON from the response
        text = response.text.strip()
        # Find the first and last brackets to extract JSON array
        start = text.find('[')
        end = text.rfind(']')
        if start != -1 and end != -1:
            json_str = text[start:end+1]
            quiz = json.loads(json_str)
            return quiz
        else:
            # Fallback: return the raw text in a single question
            return [{"question": text, "options": [], "answer": ""}]
    except Exception as e:
        return [{"question": f"Error generating quiz: {e}", "options": [], "answer": ""}]

def generate_game(lesson_text: str) -> dict:
    """
    Generates a simple educational game (e.g., fill-in-the-blank) from lesson text.

    Args:
        lesson_text: The full lesson text.

    Returns:
        Game data (e.g., sentences with blanks and answers).
    """
    # Use Vertex AI Gemini to generate a fill-in-the-blank game with multiple blanks
    prompt = f"""
    You are an educational assistant. Given the following lesson text, create a fill-in-the-blank game. Return a JSON object with:
    - 'text': a longer passage (3-5 sentences) from the lesson with 3-5 key words replaced by numbered blanks (e.g., '____1____', '____2____', ...)
    - 'answers': a list of the correct words for each blank, in order

    Lesson:
    {lesson_text}

    Format:
    {{"text": "... ____1____ ... ____2____ ... ____3____ ...", "answers": ["answer1", "answer2", "answer3"]}}
    Return only valid JSON.
    """
    try:
        model = GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        text = response.text.strip()
        # Find the first and last curly braces to extract JSON object
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1:
            json_str = text[start:end+1]
            game = json.loads(json_str)
            return game
        else:
            return {"text": text, "answers": []}
    except Exception as e:
        return {"text": f"Error generating game: {e}", "answers": []}


def suggest_video(lesson_text: str) -> str:
    """
    Suggests a YouTube video or generates a video script for the lesson.

    Args:
        lesson_text: The full lesson text.

    Returns:
        Video URL or script.
    """
    # TODO: Call Vertex AI LLM or use YouTube Data API
    return "https://youtube.com/example_video"


def save_student_progress(student_id: str, topic: str, mastery: float) -> str:
    """
    Saves or updates student progress in Firestore/BigQuery.

    Args:
        student_id: Unique student identifier.
        topic: The topic being updated.
        mastery: Mastery score (0-1).

    Returns:
        Confirmation message.
    """
    # TODO: Integrate with Firestore/BigQuery
    return f"Progress for {student_id} on {topic} saved."


def load_student_progress(student_id: str) -> dict:
    """
    Loads student progress from Firestore/BigQuery.

    Args:
        student_id: Unique student identifier.

    Returns:
        Progress data as a dict.
    """
    # TODO: Integrate with Firestore/BigQuery
    return {"photosynthesis": {"mastery": 0.8, "last_attempt": "2025-09-16"}}

def start_quiz(lesson_text: str) -> dict:
    """
    Starts a quiz session. Returns the first question and a session state dict.
    """
    questions = generate_quiz(lesson_text)
    session = {
        "questions": questions,
        "current": 0,
        "score": 0,
        "total": len(questions),
        "history": []
    }
    if not questions:
        return {"message": "No questions generated.", "session": session}
    q = questions[0]
    return {
        "question": q["question"],
        "options": q.get("options", []),
        "question_idx": 0,
        "session": session
    }

def answer_quiz(question_idx: int, user_answer: str, session: dict) -> dict:
    """
    Receives user's answer, checks correctness, updates session, and returns next question or final score.
    """
    questions = session["questions"]
    q = questions[question_idx]
    correct = (user_answer.strip() == q["answer"])
    if correct:
        session["score"] += 1
    session["history"].append({
        "question": q["question"],
        "user_answer": user_answer,
        "correct_answer": q["answer"],
        "correct": correct
    })
    next_idx = question_idx + 1
    if next_idx < session["total"]:
        next_q = questions[next_idx]
        return {
            "result": "correct" if correct else "incorrect",
            "correct_answer": q["answer"],
            "score": session["score"],
            "question": next_q["question"],
            "options": next_q.get("options", []),
            "question_idx": next_idx,
            "session": session
        }
    else:
        return {
            "result": "correct" if correct else "incorrect",
            "correct_answer": q["answer"],
            "score": session["score"],
            "finished": True,
            "total": session["total"],
            "history": session["history"]
        }

def start_game(lesson_text: str) -> dict:
    """
    Starts a fill-in-the-blank game session. Returns the sentence with blank and the answer (hidden), plus session state.
    """
    game = generate_game(lesson_text)
    session = {
        "text": game.get("text", ""),
        "answers": game.get("answers", []),
        "user_answers": [None] * len(game.get("answers", [])),
        "attempts": 0,
        "finished": False
    }
    return {
        "text": session["text"],
        "num_blanks": len(session["answers"]),
        "session": session
    }

def answer_game(user_answer: str, session: dict) -> dict:
    """
    Checks the user's answer for the fill-in-the-blank game, updates session, and returns feedback.
    """
    # user_answer should be a dict: {blank_idx: answer, ...}
    # e.g., {0: "word1", 1: "word2"}
    session["attempts"] += 1
    results = []
    all_correct = True
    for idx, correct_answer in enumerate(session["answers"]):
        user_ans = user_answer.get(idx, "").strip().lower()
        session["user_answers"][idx] = user_ans
        is_correct = (user_ans == correct_answer.strip().lower())
        results.append({
            "blank": idx+1,
            "user_answer": user_ans,
            "correct_answer": correct_answer,
            "correct": is_correct
        })
        if not is_correct:
            all_correct = False
    if all_correct:
        session["finished"] = True
    return {
        "results": results,
        "attempts": session["attempts"],
        "finished": session["finished"],
        "text": session["text"],
        "session": session
    }

import os
from pathlib import Path

def generate_minigame_code(lesson_text: str, output_dir: str = "game_generated_code") -> str:
    """
    Generates a complete HTML5 quiz-arcade minigame project in the specified output directory.
    Args:
        lesson_text: The lesson content to use for quiz/game generation.
        output_dir: The directory to write the generated code to.
    Returns:
        Path to the generated project folder.
    """
    # Prepare quiz data using existing agent logic
    quiz = generate_quiz(lesson_text)
    # Ensure output directory structure
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(f"{output_dir}/static/css").mkdir(parents=True, exist_ok=True)
    Path(f"{output_dir}/static/js").mkdir(parents=True, exist_ok=True)
    Path(f"{output_dir}/templates").mkdir(parents=True, exist_ok=True)

    # Write requirements.txt
    with open(f"{output_dir}/requirements.txt", "w", encoding="utf-8") as f:
        f.write("""flask==2.0.1\nvertexai>=0.0.1\ngoogle-cloud-storage>=2.0.0\ngoogle-auth>=2.0.0\ngoogle-adk>=1.0.0\nzoneinfo>=0.2.1\n""")

    # Write Dockerfile
    with open(f"{output_dir}/Dockerfile", "w", encoding="utf-8") as f:
        f.write("""# Stage 1: Build\nFROM python:3.9-slim as builder\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install --user -r requirements.txt\n\n# Stage 2: Runtime\nFROM python:3.9-slim\n\nWORKDIR /app\n\nCOPY --from=builder /root/.local /root/.local\nENV PATH=/root/.local/bin:$PATH\n\nCOPY . .\n\nENV GOOGLE_CLOUD_PROJECT=\"your-project-id\"\nENV GOOGLE_CLOUD_LOCATION=\"global\"\nENV GOOGLE_GENAI_USE_VERTEXAI=\"True\"\n\nEXPOSE 5000\n\nCMD [\"python\", \"app/app.py\"]\n""")

    # Write docker-compose.yml
    with open(f"{output_dir}/docker-compose.yml", "w", encoding="utf-8") as f:
        f.write("""version: '3.8'\nservices:\n  web:\n    build: .\n    ports:\n      - \"5000:5000\"\n    environment:\n      - GOOGLE_CLOUD_PROJECT=your-project-id\n      - GOOGLE_CLOUD_LOCATION=global\n      - GOOGLE_GENAI_USE_VERTEXAI=True\n""")

    # Write README.md
    with open(f"{output_dir}/README.md", "w", encoding="utf-8") as f:
        f.write("""# Lesson Quiz Arcade\n\nA browser-playable HTML5 mini-game for reviewing lesson content. Paste your lesson text, play a quiz, earn points, and unlock hints!\n\n## Quick Start\n\n```sh\ndocker build -t lesson-quiz-arcade .\ndocker run -p 5000:5000 lesson-quiz-arcade\n```\n\nOr with Docker Compose:\n\n```sh\ndocker compose up --build\n```\n\nThen open [http://localhost:5000](http://localhost:5000) in your browser.\n""")

    # Write app/agent.py (minimal stub, user can copy their logic)
    Path(f"{output_dir}/app").mkdir(parents=True, exist_ok=True)
    with open(f"{output_dir}/app/agent.py", "w", encoding="utf-8") as f:
        f.write("""# Copy your agent logic here.\n""")

    # Write app/app.py
    with open(f"{output_dir}/app/app.py", "w", encoding="utf-8") as f:
        f.write(f"""from flask import Flask, render_template, request, jsonify\nfrom agent import generate_quiz\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('game.html')\n\n@app.route('/api/quiz', methods=['POST'])\ndef quiz():\n    lesson_text = request.json.get('lesson_text', '')\n    quiz = generate_quiz(lesson_text)\n    return jsonify({{'quiz': quiz}})\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)\n""")

    # Write templates/game.html
    with open(f"{output_dir}/templates/game.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>Lesson Quiz Arcade</title>\n    <link rel=\"stylesheet\" href=\"/static/css/style.css\">\n</head>\n<body>\n    <div id=\"game-container\">\n        <h1>Lesson Quiz Arcade</h1>\n        <div id=\"upload-section\">\n            <textarea id=\"lesson-text\" placeholder=\"Paste lesson text here...\"></textarea>\n            <button id=\"start-quiz\">Start Quiz</button>\n        </div>\n        <div id=\"quiz-section\" style=\"display:none;\"></div>\n        <div id=\"score-section\" style=\"display:none;\"></div>\n    </div>\n    <script src=\"/static/js/game.js\"></script>\n</body>\n</html>\n""")

    # Write static/css/style.css
    with open(f"{output_dir}/static/css/style.css", "w", encoding="utf-8") as f:
        f.write("""body {\n    font-family: Arial, sans-serif;\n    background: #f7f7f7;\n    margin: 0;\n    padding: 0;\n}\n#game-container {\n    max-width: 600px;\n    margin: 40px auto;\n    background: #fff;\n    border-radius: 8px;\n    box-shadow: 0 2px 8px rgba(0,0,0,0.1);\n    padding: 32px;\n}\n#upload-section textarea {\n    width: 100%;\n    height: 100px;\n    margin-bottom: 12px;\n}\n#start-quiz {\n    padding: 8px 24px;\n    font-size: 1rem;\n    background: #4caf50;\n    color: #fff;\n    border: none;\n    border-radius: 4px;\n    cursor: pointer;\n}\n#quiz-section {\n    margin-top: 24px;\n}\n.quiz-question {\n    margin-bottom: 18px;\n}\n.quiz-options button {\n    margin: 4px 8px 4px 0;\n    padding: 6px 16px;\n    border: 1px solid #ccc;\n    border-radius: 4px;\n    background: #e0e0e0;\n    cursor: pointer;\n}\n.quiz-options button.correct {\n    background: #4caf50;\n    color: #fff;\n}\n.quiz-options button.incorrect {\n    background: #f44336;\n    color: #fff;\n}\n#score-section {\n    margin-top: 32px;\n    font-size: 1.2rem;\n    font-weight: bold;\n}\n""")

    # Write static/js/game.js
    with open(f"{output_dir}/static/js/game.js", "w", encoding="utf-8") as f:
        f.write("""let quizData = null;\nlet currentQuestion = 0;\nlet score = 0;\nlet hintsUnlocked = 0;\n\nfunction showQuestion() {\n    const quizSection = document.getElementById('quiz-section');\n    quizSection.innerHTML = '';\n    if (!quizData || currentQuestion >= quizData.length) {\n        document.getElementById('score-section').style.display = 'block';\n        document.getElementById('score-section').innerText = `Game Over! Your score: ${score} / ${quizData.length}`;\n        return;\n    }\n    const q = quizData[currentQuestion];\n    const qDiv = document.createElement('div');\n    qDiv.className = 'quiz-question';\n    qDiv.innerHTML = `<strong>Q${currentQuestion+1}:</strong> ${q.question}`;\n    const optionsDiv = document.createElement('div');\n    optionsDiv.className = 'quiz-options';\n    q.options.forEach(opt => {\n        const btn = document.createElement('button');\n        btn.innerText = opt;\n        btn.onclick = () => handleAnswer(opt, btn);\n        optionsDiv.appendChild(btn);\n    });\n    qDiv.appendChild(optionsDiv);\n    // Hint button\n    if (hintsUnlocked > 0) {\n        const hintBtn = document.createElement('button');\n        hintBtn.innerText = 'Show Hint';\n        hintBtn.onclick = () => {\n            hintBtn.disabled = true;\n            hintBtn.innerText = `Hint: ${q.answer}`;\n        };\n        qDiv.appendChild(hintBtn);\n    }\n    quizSection.appendChild(qDiv);\n    quizSection.style.display = 'block';\n}\n\nfunction handleAnswer(selected, btn) {\n    const q = quizData[currentQuestion];\n    const options = btn.parentElement.querySelectorAll('button');\n    options.forEach(b => b.disabled = true);\n    if (selected === q.answer) {\n        btn.classList.add('correct');\n        score++;\n        if (score % 2 === 0) hintsUnlocked++;\n    } else {\n        btn.classList.add('incorrect');\n        // Optionally show correct answer\n        options.forEach(b => {\n            if (b.innerText === q.answer) b.classList.add('correct');\n        });\n    }\n    setTimeout(() => {\n        currentQuestion++;\n        showQuestion();\n    }, 900);\n}\n\ndocument.getElementById('start-quiz').onclick = async function() {\n    const lessonText = document.getElementById('lesson-text').value;\n    if (!lessonText.trim()) return alert('Please paste lesson text!');\n    const resp = await fetch('/api/quiz', {\n        method: 'POST',\n        headers: {'Content-Type': 'application/json'},\n        body: JSON.stringify({lesson_text: lessonText})\n    });\n    const data = await resp.json();\n    quizData = data.quiz;\n    currentQuestion = 0;\n    score = 0;\n    hintsUnlocked = 0;\n    document.getElementById('upload-section').style.display = 'none';\n    document.getElementById('score-section').style.display = 'none';\n    showQuestion();\n};\n""")

    return str(Path(output_dir).resolve())

>>>>>>> e35e7c2 (Initial commit)


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
<<<<<<< HEAD
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[get_weather, get_current_time],
=======
    instruction="You are a helpful AI assistant designed to provide accurate and useful information and educational support.",
    tools=[
        extract_text_from_file,
        extract_key_concepts,
        generate_minigame_code,
        suggest_video,
        save_student_progress,
        load_student_progress,
        start_quiz,
        answer_quiz,
        start_game,
        answer_game,
    ],
>>>>>>> e35e7c2 (Initial commit)
)
