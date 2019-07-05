
# Module imports
from datetime import datetime
from jenkins_exceptions import JenkinsException, JenkinsAuthorizationException

import json
import requests
import sqlite3 as sq

DB_NAME = "jenkins_jobs.db"

# Create SQLite Database and tables if they don't already exist
db = sq.connect(DB_NAME)
cursor = db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Job (ID INTEGER PRIMARY KEY, name, status, checked_at DATE)"
)
db.commit()


class Jenkins:
    """
    Jenkins class for connecting and communicating 
    with a Jenkins server

    :param username: the username on the jenkins server
    :param pwd_or_token: the password or token on the jenkins server
    :param server_domain: the domain of the jenkins server
    :param server_port: the port number of the jenkins server
    """

    # url string that represents the url from which the jobs
    # details (name and build result) are gotten from.
    # Defined as a class attribute
    builds_url = "/api/json?tree=jobs[name,builds[result]]"

    def __init__(self,
                 username: str,
                 pwd_or_token: str,
                 server_domain: str = 'localhost',
                 server_port: int = 8080):
        self.username = username
        self.pwd_or_token = pwd_or_token
        self.server_domain = server_domain
        self.server_port = server_port

        self.url = self.__make_jenkins_url()

    def __make_jenkins_url(self):
        """
        Make a fully qualified URL for connecting to the Jenkins server
        """

        return f"http://{self.username}:{self.pwd_or_token}@{self.server_domain}:{self.server_port}/"

    @staticmethod
    def save_job_details(name, status):
        """
        Saves the job's details(name and status) to
        the database
        """
        try:
            cursor.execute(
                "INSERT INTO Job (name, status, checked_at) VALUES(?,?,?)", (
                    name,
                    status,
                    datetime.now(),
                ))
            db.commit()
        except sq.OperationalError:
            raise

    def get_details(self):
        """
        Function that gets all the jobs in the Jenkins instance
        and then the status (result) of each job, if any
        
        TC: n^2
        """

        # Try to get all the jobs and their details
        jobs = requests.get(self.url + self.__class__.builds_url)

        # If it's successful
        if jobs.status_code == 200:
            # Get a list of the jobs and their details (name, builds, etc.)
            jobs = jobs.json().get('jobs')

            # For each job
            for job in jobs:
                # For each build in the job's builds list
                for build in job.get('builds'):
                    # Save the name of the job and the build status of the job's build
                    self.save_job_details(job.get('name'), build.get('result').capitalize())

            # Finally close the database
            db.close()

        # Incase of wrong credentials
        elif jobs.status_code in (401, 403):
            raise JenkinsAuthorizationException("Invalid credentials")
        
        # Other kinds of errors, generically categorized
        else:
            raise JenkinsException("An error occured")

        # Echo notification
        print(f"Success: Saved details to database {DB_NAME}")


    def __repr__(self):
        """JSON-like representation of the object"""

        return json.dumps(vars(self))

