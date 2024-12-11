# Flask Application with CI/CD Pipeline

This is a simple Flask application that demonstrates CI/CD using GitHub Actions. The application provides an endpoint to add numbers and includes comprehensive testing.

## Features

- REST API endpoint for adding numbers
- Support for both positive and negative numbers
- Comprehensive test suite
- CI/CD pipeline using GitHub Actions

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests locally:
```
pytest app_test.py -v
```

## CI/CD Pipeline

The GitHub Actions workflow is configured to:
- Run on push to main and feature/tests branches
- Run on pull requests to main
- Install dependencies
- Run the test suite

## API Usage

POST `/add`
```json
{
    "numbers": [1, 2, 3]
}
```

Response:
```json
{
    "result": 6
}
```
