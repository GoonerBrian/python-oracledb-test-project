# python-oracledb-test-project

This purpose of this repo is simply to test and play with connecting
to the CISE Oracle DB and getting the results of simple queries.

# Setup

- Connect to UF VPN
- Connect to CISE Oracle DB through Oracle SQL Developer
- Create a simple table in the DB and populate it with some dummy data
- Run the following to install the oracledb package
  ```
  python3 -m pip install oracledb
  ```
- Run the following to install the dotenv package

  ```
  python3 -m pip install python-dotenv
  ```

- Create a `.env` fill in the same directory as `test.py` with the following contents:

  ```
  USER_NAME = "john.doe"
  DB_USER_NAME = "JOHN.DOE"
  DB_PASSWORD = "password"
  TABLE_NAME = "What_ever_your_table_name_is"
  ```

- Run the following to run the script

  ```
  python3 test.py
  ```

_Note: `python3` can be changed to `python` if `python3` is already your default python version_
