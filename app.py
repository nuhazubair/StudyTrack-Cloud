from flask import Flask, request, redirect

app = Flask(__name__)

assignments = [
    {"subject": "Cloud Computing", "task": "CA1 - SaaS & PaaS Application", "status": "In Progress"},
    {"subject": "Database Management", "task": "SQL Practical", "status": "Completed"},
    {"subject": "Network Essentials", "task": "Network Assignment", "status": "Pending"}
]


@app.route("/")
def home():

    assignment_rows = ""

    for index, assignment in enumerate(assignments):
        assignment_rows += f"""
        <tr>
    <td>{assignment['subject']}</td>
    <td>{assignment['task']}</td>
    <td>{assignment['status']}</td>
    <td>
        <a href="/delete/{index}">Delete</a>
    </td>
</tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>StudyTrack Cloud</title>

        <style>
            body {{
                font-family: Arial;
                background-color: #f4f7fb;
                margin: 0;
            }}

            .header {{
                background-color: #2563eb;
                color: white;
                padding: 25px;
            }}

            .container {{
                padding: 30px;
            }}

            .card {{
                background-color: white;
                padding: 25px;
                margin-bottom: 20px;
                border-radius: 10px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            th, td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }}

            th {{
                background-color: #e8eefc;
            }}

            input, select {{
                width: 100%;
                padding: 10px;
                margin: 8px 0 15px 0;
                box-sizing: border-box;
            }}

            button {{
                background-color: #2563eb;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 6px;
                cursor: pointer;
            }}

            button:hover {{
                background-color: #1d4ed8;
            }}
        </style>

    </head>

    <body>

        <div class="header">
            <h1>StudyTrack Cloud</h1>
            <p>Student Study & Assignment Tracker</p>
        </div>

        <div class="container">

            <div class="card">
                <h2>Dashboard</h2>
                <p>Welcome to StudyTrack Cloud.</p>
                <p>Manage your subjects, assignments and study progress in one place.</p>
            </div>

            <div class="card">

                <h2>Add Assignment</h2>

                <form method="POST" action="/add">

                    <label>Subject</label>
                    <input type="text" name="subject" required>

                    <label>Assignment</label>
                    <input type="text" name="task" required>

                    <label>Status</label>

                    <select name="status">
                        <option>Pending</option>
                        <option>In Progress</option>
                        <option>Completed</option>
                    </select>

                    <button type="submit">Add Assignment</button>

                </form>

            </div>

            <div class="card">

                <h2>My Assignments</h2>

                <table>

                    <tr>
                        <th>Subject</th>
                        <th>Assignment</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>

                    {assignment_rows}

                </table>

            </div>

        </div>

    </body>
    </html>
    """


@app.route("/add", methods=["POST"])
def add_assignment():

    subject = request.form["subject"]
    task = request.form["task"]
    status = request.form["status"]

    assignments.append({
        "subject": subject,
        "task": task,
        "status": status
    })

    return redirect("/")


@app.route("/delete/<int:index>")
def delete_assignment(index):

    if 0 <= index < len(assignments):
        assignments.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run()