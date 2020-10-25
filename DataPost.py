class DataPost():
    """docstring for DataPost."""

    def __init__(self):

        super(DataPost, self).__init__()

    def PostToKillGorack(self, results):

        with open('key.txt') as f:
            first_line = f.readline()
        results['key'] = first_line
        results['app'] = "speedtest"
        import requests
        import json
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post('https://www.killgorack.com/portal-x/all/fn/RawDataService.php', data=results, verify=True)
        print(response.text)
