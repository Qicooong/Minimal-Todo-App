# server.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy database object
db = SQLAlchemy(app)

# Define Todo item model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    due_date = db.Column(db.DateTime, nullable=True)
    priority = db.Column(db.Integer, default=0)
    position = db.Column(db.Integer, nullable=False, default=0) # New: Position for ordering

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'is_completed': self.is_completed,
            'created_at': self.created_at.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'priority': self.priority,
            'position': self.position # Include position in dict
        }

# --- API Interface Definitions ---

# Get all todo items
@app.route('/todos', methods=['GET'])
def get_todos():
    # Query all todo items, order by position, then by creation time for tie-breaking
    todos = Todo.query.order_by(Todo.position.asc(), Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos])

# Add a new todo item
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    if not data or 'content' not in data or not data['content'].strip():
        return jsonify({"error": "Content is required"}), 400

    # Get the maximum current position and add 1 for the new todo
    max_position = db.session.query(db.func.max(Todo.position)).scalar()
    new_position = (max_position if max_position is not None else -1) + 1

    new_todo = Todo(
        content=data['content'].strip(),
        due_date=datetime.datetime.fromisoformat(data['due_date']) if 'due_date' in data and data['due_date'] else None,
        priority=data.get('priority', 0),
        position=new_position # Set initial position
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# Update a todo item
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.json

    if 'content' in data:
        todo.content = data['content'].strip()
    if 'is_completed' in data:
        todo.is_completed = data['is_completed']
    if 'due_date' in data:
        todo.due_date = datetime.datetime.fromisoformat(data['due_date']) if data['due_date'] else None
    if 'priority' in data:
        todo.priority = data['priority']
    if 'position' in data: # Allow updating position directly
        todo.position = data['position']

    db.session.commit()
    return jsonify(todo.to_dict())

# New API endpoint for reordering todos
@app.route('/todos/reorder', methods=['PUT'])
def reorder_todos():
    data = request.json
    if not data or 'ordered_ids' not in data or not isinstance(data['ordered_ids'], list):
        return jsonify({"error": "Invalid request. 'ordered_ids' (list of integers) is required."}), 400

    ordered_ids = data['ordered_ids']
    
    # Fetch all todos that are being reordered to ensure they exist
    todos_map = {todo.id: todo for todo in Todo.query.filter(Todo.id.in_(ordered_ids)).all()}

    if len(todos_map) != len(ordered_ids):
        # This means some IDs in the list were not found in the database
        return jsonify({"error": "One or more todo IDs not found."}), 404

    # Update positions based on the new order
    for index, todo_id in enumerate(ordered_ids):
        todo = todos_map[todo_id]
        todo.position = index # Assign new position based on list index

    db.session.commit()
    return jsonify({"message": "Todos reordered successfully."}), 200

# Delete a todo item
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

# Run Flask application
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables if they don't exist
    app.run(debug=True, host='0.0.0.0', port=5000)
