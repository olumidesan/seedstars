
from datetime import datetime
from jenkins_exceptions import JenkinsException, JenkinsAuthorizationException

import json
import requests
import sqlite3 as sq


DB_NAME = "jenkins_jobs.db"

db = sq.connect(DB_NAME)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Job (ID INTEGER PRIMARY KEY, name, status, checked_at DATE)")
db.commit()


class Jenkins:
    """
    Jenkins class for connecting and communicating 
    with a Jenkins server

    :param username: the username of the jenkins instance
    :param password: the password of the jenkins instance
    :param server_domain: the domain of the jenkins instance
    :param server_port: the port number of the jenkins instance
    """

    # Class attributes 
    jobs_pathname = "api/json?tree=jobs[name]"
    build_status_pathname = "/api/json?tree=builds[result]"

    def __init__(self, username:str, pwd_or_token:str, server_domain:str='localhost', server_port:int=8080):
        self.username = username
        self.pwd_or_token = pwd_or_token
        self.server_domain = server_domain
        self.server_port = server_port

        self.url = self.__make_jenkins_url()
    
    def __make_jenkins_url(self):
        return f"http://{self.username}:{self.pwd_or_token}@{self.server_domain}:{self.server_port}/"

    @staticmethod
    def save_job_details(name, status):
        """
        Saves the job's details(name and status) to
        the database
        """

        try:
            cursor.execute("INSERT INTO Job (name, status, checked_at) VALUES(?,?,?)", (name, status, datetime.now(),))
            db.commit()
        except sq.OperationalError:
            raise 

    def get_details(self):
        """
        Function that gets all the jobs in the Jenkins instance
        and then the status (result) of each job, if any
        """

        jobs = requests.get(self.url + self.__class__.jobs_pathname)

        if jobs.status_code == 200:
            all_jobs = [ job['name'] for job in jobs.json().get('jobs') ]

            for name in all_jobs:
                builds =  requests.get(self.url + f"/job/{name}" + self.__class__.build_status_pathname).json().get('builds')
                for build in builds:
                    self.save_job_details(name, build.get('result').capitalize())
            
            db.close()

        elif jobs.status_code in (401, 403):
            raise JenkinsAuthorizationException("Invalid credentials")

        else:
            raise JenkinsException("An error occured")
    
        return "Done"

    def __repr__(self):
        """JSON-like representation of the object"""

        return json.dumps(vars(self))

j = Jenkins('olumide', 'Femi1610_')
print(j.get_details())
