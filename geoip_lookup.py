import socket
from geoip import geolite2
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get IP Geolocation info')
    parser.add_argument('--hostname', action='store', dest='hostname', required=True)

    given_args = parser.parse_args()
    hostname = given_args.hostname
    ip_address = socket.gethostbyname(hostname)
    print('IP address: {0}'.format(ip_address))

    match = geolite2.lookup(ip_address)
    """if match is not None :
        print("Country: {0}\nContinent: {1}\nTime zone: {2}"\
        .format(match.country, match.continent, match.timeozone))
        """
