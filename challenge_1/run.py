

from getpass import getpass
from jenkins import Jenkins

if __name__ == '__main__':
    # Main script
    username = input("Enter the username of your Jenkins instance: ")
    password = getpass("Enter the password or token for the Jenkins instance: ")

    kwargs = dict(username=username, pwd_or_token=password)

    domain = input("Enter the domain name of your Jenkins instance defaults to 'localhost' if you just press Enter): ")

    while 1:
        port = input("Enter the port of your Jenkins instance (defaults to 8080 if you just press Enter): ")
        # If Enter was pressed
        if not port:
            break 
        try:
            int(port)
        except ValueError:
            print("Error: The port number must be an integer\n")
            continue
        else:
            break

    if domain:
        kwargs.update(dict(server_domain=domain)) 
    if port:
        kwargs.update(dict(server_port=port))

    j = Jenkins(**kwargs)
    j.get_details()
