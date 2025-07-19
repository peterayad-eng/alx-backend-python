# 0x03-Unittests_and_integration_tests

This directory contains solutions for the "Unittests and Integration Tests" project.

## Task 0: Parameterize a unit test

This task involves writing a parameterized unit test for the `utils.access_nested_map` function.

### Files:
- `utils.py`: Contains the `access_nested_map` function.
- `test_utils.py`: Contains the `TestAccessNestedMap` class with the `test_access_nested_map` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_utils.py
```
---
## Task 1: Parameterize a unit test (Exception Handling)

This task involves writing a parameterized unit test for the `utils.access_nested_map` function to test exception handling.

### Files:
- `test_utils.py`: Updated to include `test_access_nested_map_exception` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_utils.py
```
---
## Task 2: Mock HTTP Calls

This task involves writing a unit test for the `utils.get_json` function using mocking to avoid actual HTTP calls.

### Files:
- `test_utils.py`: Updated to include `TestGetJson` class with `test_get_json` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_utils.py
```
---
## Task 3: Parameterize and Patch

This task involves testing the `utils.memoize` decorator using mocking.

### Files:
- `test_utils.py`: Updated to include `TestMemoize` class with `test_memoize` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_utils.py
```
---
## Task 4: Parameterize and Patch as Decorators

This task involves testing the `GithubOrgClient.org` method using `@patch` and `@parameterized.expand` decorators.

### Files:
- `client.py`: Contains the `GithubOrgClient` class.
- `test_client.py`: Contains the `TestGithubOrgClient` class with `test_org` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_client.py
```
---
## Task 5: Mocking a property

This task involves unit-testing `GithubOrgClient._public_repos_url` by mocking `GithubOrgClient.org`.

### Files:
- `test_client.py`: Updated to include `test_public_repos_url` method.

### How to run the tests:
Navigate to the `0x03-Unittests_and_integration_tests` directory and run:
```bash
python3 -m unittest test_client.py
```
---

