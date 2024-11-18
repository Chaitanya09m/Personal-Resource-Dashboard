import subprocess

def ping_host(host):
    """
    Ping a host to check if it is reachable.
    :param host: Hostname or IP address (e.g., 'google.com').
    :return: True if the host is reachable, False otherwise.
    """
    try:
        output = subprocess.check_output(["ping", "-n", "4", host], stderr=subprocess.STDOUT, universal_newlines=True)
        return f"Host {host} is reachable.\n\n{output}"
    except subprocess.CalledProcessError:
        return f"Host {host} is not reachable."

def traceroute(host):
    """
    Perform a traceroute to a host.
    :param host: Hostname or IP address (e.g., 'google.com').
    :return: The traceroute output.
    """
    try:
        output = subprocess.check_output(["tracert", host], stderr=subprocess.STDOUT, universal_newlines=True)
        return f"Traceroute to {host}:\n\n{output}"
    except subprocess.CalledProcessError as e:
        return f"Traceroute to {host} failed.\n\n{e.output}"
if __name__ == "__main__":
    host = "google.com"
    print("Pinging host:")
    print(ping_host(host))

    print("\nTraceroute:")
    print(traceroute(host))
