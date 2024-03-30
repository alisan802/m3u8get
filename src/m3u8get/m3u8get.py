import requests
import json
from urllib.parse import urlparse, urljoin


def http_get(url) -> bytes:
    proxies = None
    req = requests.get(url, proxies=proxies)
    return req.content


def m3u8get(m3u8url) -> None:
    m3u8 = http_get(m3u8url)
    m3u8_filename = str(urlparse(m3u8url).path).split('/')[-1]
    print(m3u8_filename)
    with open(m3u8_filename, 'wb') as m3u8_file:
        m3u8_file.write(m3u8)
    for m3u8line in m3u8.decode('utf-8').splitlines():
        if m3u8line.startswith('#'):
            pass
        else:
            video_url = urljoin(m3u8url, m3u8line)
            print(video_url)
            video = http_get(video_url)
            with open(m3u8line, 'wb') as video_file:
                video_file.write(video)
    return


def ip_host() -> dict:
    import time
    ip_host_resp = json.loads(
        http_get(
            url='https://ifconfig.io/all.json'
        )
    )
    # The host information in all.json seems to be wrong.
    # Overwrite the result with the correct host information.
    host = http_get(url='https://ifconfig.io/host')
    ip_host_resp['host'] = host.decode('utf-8').strip()
    if __name__ == '__main__':
        # Output the results.
        print('========== SHOW IP HOST INFO ==========')
        for key, value in ip_host_resp.items():
            print('{} : {}'.format(str(key).upper(), value))
        print(' ... Waiting 10 sec to review host information.')
        time.sleep(10)
    return ip_host_resp


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Get m3u8 video file.')
    parser.add_argument(
        'm3u8url', metavar='URL', type=str,
        help='HTTP URL of m3u8 file'
    )
    parser.add_argument(
        '--show-ip-host', action='store_true', default=False,
        help='Show IP Host Information'
    )
    args = parser.parse_args()
    if args.show_ip_host:
        ip_host()
    else:
        pass
    m3u8get(args.m3u8url)


if __name__ == '__main__':
    main()
