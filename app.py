from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS_AND_ANSWERS = {
    "football": {
        "question": "Does the college have a football team?",
        "answer": "Yes, the college has a football team and participates in intercollegiate athletics."
    },
    "cs": {
        "question": "Does it offer a Computer Science major?",
        "answer": "Yes, the college offers a Computer Science major with courses in programming, databases, networking, and software development."
    },
    "tuition": {
        "question": "What is the in-state tuition?",
        "answer": "The in-state tuition is approximately $10,000 per academic year. Please check the official college website for the most current amount."
    },
    "housing": {
        "question": "Does it provide on-campus housing?",
        "answer": "Yes, the college provides on-campus housing options for eligible students."
    }
}

CREATOR_INFO = {
    "first_name": "Harika",
    "last_name": "Pinninti",
    "email": "pinninha@mail.uc.edu"
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_answer = None
    selected_question = None
    user_info = {
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    if request.method == "POST":
        user_info["first_name"] = request.form.get("first_name", "")
        user_info["last_name"] = request.form.get("last_name", "")
        user_info["email"] = request.form.get("email", "")
        selected_key = request.form.get("question")

        if selected_key in QUESTIONS_AND_ANSWERS:
            selected_question = QUESTIONS_AND_ANSWERS[selected_key]["question"]
            selected_answer = QUESTIONS_AND_ANSWERS[selected_key]["answer"]

    return render_template(
        "index.html",
        questions=QUESTIONS_AND_ANSWERS,
        selected_question=selected_question,
        selected_answer=selected_answer,
        user_info=user_info,
        creator=CREATOR_INFO
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)