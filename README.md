# College Bootcamp Project

This is a college bootcamp project designed to demonstrate the integration of modern web development technologies.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Tech Stack

The project is built using the following technologies:

- **Frontend**:
  - HTML
  - CSS
  - JavaScript
  - React

- **Backend**:
  - Node.js
  - FastAPI


## Features

- Responsive web design using ReactJS.
- Backend API built with FastAPI.
- Cross-Origin Resource Sharing (CORS) enabled for seamless frontend-backend communication.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Viverun/College-bootcamp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd College-Bootcamp
   ```

3. Install dependencies for the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Install dependencies for the frontend:
   ```bash
   cd ../frontend
   npm install
   ```

## Usage

1. Start the backend server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. Start the frontend development server:
   ```bash
   cd ../frontend
   npm run dev
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5173
   ```

## Project Structure

```
College-Bootcamp/
│
├── backend/               # Backend application (FastAPI)
│   ├── main.py           # Main backend application
│   ├── pyproject.toml    # Python project configuration
│   ├── requirements.txt  # Python dependencies
│   └── ...
│
├── frontend/              # Frontend application (React)
│   ├── src/              # Source files
│   ├── public/           # Static files
│   ├── package.json      # Node.js dependencies
│   └── ...
│
└── README.md              # Project documentation
```