import subprocess

def execPing(hostName, attempts, waitTime):
    boop = subprocess.Popen(
        ["ping", "-c " + attempts, "-W " + waitTime, hostName],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )
    out, error = boop.communicate()
    success = out.decode('utf-8').replace('\r', '')
    fail = error.decode('utf-8').replace('\r', '')

    if success is not "":
        if "Request timeout" in success:
            return ("Request timeout: ", success)
        return ("Success: ", success)
    elif fail is not "":
        return ("Failed: ", fail)
