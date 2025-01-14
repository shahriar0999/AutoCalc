# Simple Calculator with CI/CD Integration

This is a simple calculator API built with **FastAPI**, designed as a learning project to practice **Continuous Integration (CI)** and **Continuous Deployment (CD)** workflows. Currently, the project includes basic mathematical operations, automated tests using **pytest**, and a CI pipeline set up with GitHub Actions. CD implementation will be added in the future.

---

## Features

- Basic calculator operations (e.g., addition, subtraction, square operation, etc.)
- Built using **FastAPI** for a lightweight and high-performance API.
- Automated testing with **pytest** to ensure code quality.
- CI pipeline using GitHub Actions to test and build the project.
- Docker support for containerized deployments.

---

## Installation

### Prerequisites
- Python 3.9+
- Docker (optional, for containerized builds)
- pip (Python package manager)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/shahriar0999/AutoCalc.git
   cd AutoCalc

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the FastAPI app:
   ```bash
   python main.py

4. Open your browser and go to http://127.0.0.1:8000/docs to access the interactive API documentation.


### Testing
#### This project uses pytest for testing. To run tests:

1. Install pytest if not already installed:
   ```bash
   pip install pytest

2. Run tests:
   ```bash
   pytest tests/test_app.py


## CI/CD Workflow
### CI Workflow
The CI workflow is implemented using GitHub Actions. It runs the following steps on every push to the main branch:

- Checks out the code.
- Sets up the Python environment (Python 3.9).
- Installs dependencies from requirements.txt.
- Runs the tests using pytest.
- Builds a Docker image.
- Pushes the Docker image to Docker Hub.


### Future Enhancements
- Add Continuous Deployment (CD) to deploy the application automatically to AWS.
- Expand the calculator's functionality to include more advanced operations.