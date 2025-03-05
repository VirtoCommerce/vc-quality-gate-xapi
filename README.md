
# vc-quality-gate-xapi


## Overview
This project is an API testing framework using **Python + Playwright**. It allows testing **REST APIs and GraphQL APIs** efficiently with automated scripts.

## Prerequisites
Before setting up the project, ensure you have the following installed:
- **Python** (>= 3.8)
- **pip** (Python package manager)
- **Node.js** (Required for Playwright)

## Installation
Follow these steps to set up the project:

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
Playwright requires browsers to be installed for web interactions.
```bash
playwright install
```

## Configuration
### 1. Set Up Environment Variables
Create a `.env` file and add the necessary variables:
```ini
BASE_URL=<API_BASE_URL>
AUTH_TOKEN=<YOUR_AUTH_TOKEN>
```

## Running Tests

### 1. Run All Tests
```bash
pytest
```

### 2. Run a Specific Test File
```bash
pytest tests/test_example.py
```

### 3. Run Tests with Verbose Output
```bash
pytest -v
```

### 4. Run Tests with Playwright Debug Mode
```bash
pytest --headed  # Runs Playwright tests with UI
```

## Project Structure
```
.
├── tests/                # Test scripts
│   ├── test_api.py       # API test example
│   ├── test_graphql.py   # GraphQL test example
├── utils/                # Utility functions
├── .env                  # Environment variables (excluded in .gitignore)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── pytest.ini            # Pytest configuration
```

## Additional Playwright Commands
- **Show browsers Playwright supports**:
  ```bash
  playwright install --list
  ```
- **Run tests in headless mode (default behavior)**:
  ```bash
  pytest --headless
  ```

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the [MIT License](LICENSE).