
# COMP3161 - Database Management Systems: 
## Final project part II


### This part of the assignment consists of two parts:

The **first part** will be a document that will consist of the ER Diagram that was chosen as the best for the implementation of the application, the tables before normalization, the list of functional dependencies and the set of normalized tables. You should clearly indicate which keys are to be used asthe primary keys. Your normalized tables should be in at least 3NF, and where possible BCNF. Youshould also include a data dictionary, describing the intended meaning of the various tables andattribute names used in the tables.



### The second part will be the application. The choice of front end is up to you. The requirements for the application are as follows:

1. You should ensure that all the basic requirements from Assignment 1 are done.
2.  You must use at least 3 stored procedures in your queries.
3.  You should provide the script used to populate your tables (not the SQL file). Include this file in the document created in the     first part of this assignment.
4. You should provide an admin interface that can at least get a report of all users and their friends along with their associated posts and comments.
5. You should have at least 500,000 users in your database to facilitate testing the requirements.

### Running the application

1. Clone the repo
  ```
  $ git clone https://github.com/MidoriRobin/comp3161-finalproject.git
  $ cd comp3161-finalproject
  ```

2. Initialize and activate a virtualenv(from the terminal):
  ```
  $ python3 -m venv venv(you only need to do this the very first time)
  $ .venv/scripts/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python3 run.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)
