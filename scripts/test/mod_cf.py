#!/usr/bin/python3


import CloudFlare

def main():
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['1d4ed24975cbac674461013ae56daba1']
        zone_name = zone['smartdirectpath.info']
        print(zone_id, zone_name)

if __name__ == '__main__':
    main()
