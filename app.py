from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

# Route for the home page
@app.route('/')
def index():
    # Render HTML template and pass the tasks list to the template
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        # Add the task to the list with a 'completed' status of False
        tasks.append({'task': task, 'completed': False})
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == '__main__':
    # Run the app in debug mode on all available IP addresses and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)