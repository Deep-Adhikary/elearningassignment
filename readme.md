# Bugs Discovered Summary

## Landing Page
### 1. Incorrect page count mentioned
- **Impact: LOW**
  - Description: The text mentions three pages, but only two exist—likely a typo, causing minor confusion.

## Case Page
### 2. Score displays invalid data (Date format)
- **Impact: HIGH**
  - Description: Users are unable to view their scores after completing the learning, as scores are incorrectly displayed in a date format.

### 3. Misdirection to learning modules
- **Impact: HIGH**
  - Description: Both cases erroneously direct to Learning 1. Learning 2 is inaccessible from the landing page.

### 4. Progress bar inaccuracies
- **Impact: LOW**
  - Description: The progress bar incorrectly updates for both courses after completing just one. This issue is not critical as it does not impede progress.

## Learning 1
### 5. Response mismatch on judgement page
- **Impact: HIGH**
  - Description: Selecting 'Guilty' shows a response for 'Not Guilty' and vice versa, providing incorrect feedback to the user.

# Folder Structure

```
.
├── LICENSE
├── readme.md
├── reports
├── requirement.txt
└── src
    ├── features
    │   ├── actions
    │   │   ├── base_action.py
    │   │   └── __init__.py
    │   ├── behave.ini
    │   ├── elearning.feature
    │   ├── environment.py
    │   ├── __init__.py
    │   ├── repository
    │   │   ├── ajax_form.py
    │   │   ├── base_page.py
    │   │   ├── __init__.py
    │   │   ├── landing_page.py
    │   │   └── project_page.py
    │   ├── steps
    │   │   ├── elearning.py
    │   │   └── __init__.py
    │   └── utils
    │       ├── data_reader
    │       │   └── csv_data_reader.py
    │       ├── enums.py
    │       ├── __init__.py
    │       ├── screenshot.py
    │       ├── types.py
    │       └── webdriver_builder
    │           ├── driver_builder.py
    │           └── __init__.py
    └── __init__.py
```

# Setup Instructions

## Prerequisites
- **Python**: Install Python 3.10 or above.
- **Dependencies**: Install required Python packages.
  ```shell
  pip install -r requirement.txt
  ```
- **Java**: Ensure Java is installed and both `PATH` and `JAVA_HOME` are configured for allure report generation.

## Execution Instructions
- **Navigate to the Features Directory**:
  ```shell
  cd src/features/
  ```
- **Execute Tests**:
  ```shell
  behave
  ```

## Generate Reports
- **Navigate to Framework Root**:
  ```shell
  cd ../..
  ```
- **Generate and View Report**:
  ```shell
  allure generate && allure open
  ```
  The report will be served locally. Open your browser to view it.

# Future Improvements
- Design comprehensive end-to-end test scripts.
- Implement the repository/action model for more robust page object handling.
- Reorganize test cases and improve folder structure for better maintainability.
- Conduct thorough scans of the application to identify additional bugs.
- **API Testing Considerations**:
  - Due to the absence of API specifications and the APIs being embedded within JavaScript, it is challenging and time-consuming to extract and test these APIs. Therefore, API testing has been excluded for now but may be included in future scopes.

# Application Feedback: Test Automation Readiness

- **Lack of Automation-Friendly Design**:
  - The current design of the application is not conducive to test automation. Key issues include:
    - **Absence of Data Attributes**: There are no `data-test-id` attributes, which are crucial for stable and reliable selector strategies in automated tests.
    - **Dynamic Element IDs**: Element IDs are dynamic and change with each session, rendering them non-reusable across different test runs.
  - **Recommendation for CI/CD**:
    - To facilitate continuous integration and delivery (CI/CD) and to enable faster feedback loops, it is essential that the application code adheres to test automation standards. Implementing static identifiers like `data-test-id` or stable, predictable element IDs would significantly improve the testability of the application.


