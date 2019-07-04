
### Get Jenkins jobs and statuses


#### Requirements
- The only requirement for this script is the Python `requests` module. Before anything, kindly install it using `pip3 install requests`.


#### Usage
- Run the `run.py` file. i.e `python3 run.py`. It will ask for the credentials to your Jenkins server -- your name, password (or token), and the server's domain name and port.


#### Note
The question said to create the script __from a given Jenkins__ instance. I figured passing an existing Jenkins instance to a Python script would cause trouble as I may not even know what language the Jenkins instance was created from, that's why instead of asking the user to pass a Jenkins instance, I'm instead requiring the user to create the Jenkins instance using my own API.