# Todo App

This is a simple Todo application with a React frontend and a Flask backend. The backend provides an API with JSON data for the frontend to consume and display.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Group Project Guidelines](#group-project-guidelines)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Project Overview

The Todo App is designed to help users manage their tasks. Users can create, read, update, and delete todo items. The frontend is built using Next.js, and the backend is built using Flask and PostgreSQL.

## Project Structure

```bash
todo-app/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── routes/
│ │ │ ├── init.py
│ │ │ ├── todos.py
│ │ └── models.py
│ │ └── config.py
│ │ └── utils.py
│ ├── migrations/
│ ├── tests/
│ │ ├── init.py
│ │ └── test_app.py
│ ├── venv/
│ ├── requirements.txt
│ └── run.py
├── frontend/
├── .gitignore
├── README.md
└── docker-compose.yml
```

## Setup Instructions

### Backend

1. Navigate to the `backend/` directory.
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python run.py
   ```

### Frontend

1. Navigate to the `frontend/` directory.
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the local development server:
   ```sh
   npm run dev
   ```
4. Build the app for deployement:
   ```sh
   npm run build
   ```

## Group Project Guidelines

1. **Collaboration**: Emphasize teamwork and communication. Regularly discuss progress and challenges with the team.
2. **Original Work**: Ensure that all code contributions are original and avoid plagiarism.
3. **Code Reviews**: Conduct code reviews to maintain code quality and share knowledge among team members.
4. **Task Management**: Use a project management tool to track tasks and assign responsibilities.
5. **Documentation**: Keep documentation up-to-date to help onboard new team members and maintain clarity.
6. **Testing**: Write tests for your code to ensure functionality and prevent future issues.
7. **Version Control**: Use Git for version control. Create branches for features and merge them through pull requests.

## API Endpoints

Here is a summary of the main API endpoints provided by the backend:

- **GET /todos**: Retrieve all todo items.
- **POST /todos**: Create a new todo item.
- **GET /todos/:id**: Retrieve a specific todo item by ID.
- **PUT /todos/:id**: Update a specific todo item by ID.
- **DELETE /todos/:id**: Delete a specific todo item by ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
