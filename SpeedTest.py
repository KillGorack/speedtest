class SpeedTest():
    """docstring for SpeedTest."""

    def __init__(self):
        super(SpeedTest, self).__init__()

    def Test(self):
        import speedtest
        from datetime import datetime

        servers = []
        threads = None

        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()

        flds = {
        'download' : round(s.results.dict()['download'] / 1000000, 3),
        'upload' : round(s.results.dict()['upload'] / 1000000, 3),
        'ping' : s.results.dict()['ping'],
        'timestamp' : datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        'bytes_sent' : s.results.dict()['bytes_sent'],
        'bytes_received' : s.results.dict()['bytes_received'],
        'share' : s.results.dict()['share']
        }

        flds_server = {
        's_url' : s.results.dict()['server']['url'],
        's_lat' : s.results.dict()['server']['lat'],
        's_lon' : s.results.dict()['server']['lon'],
        's_name' : s.results.dict()['server']['name'],
        's_country' : s.results.dict()['server']['country'],
        's_cc' : s.results.dict()['server']['cc'],
        's_sponsor' : s.results.dict()['server']['sponsor'],
        's_isp_id' : s.results.dict()['server']['id'],
        's_host' : s.results.dict()['server']['host'],
        's_d' : s.results.dict()['server']['d'],
        's_latency' : s.results.dict()['server']['latency']
        }

        flds_client = {
        'c_ip' : s.results.dict()['client']['ip'],
        'c_lat' : s.results.dict()['client']['lat'],
        'c_lon' : s.results.dict()['client']['lon'],
        'c_isp' : s.results.dict()['client']['isp'],
        'c_isprating' : s.results.dict()['client']['isprating'],
        'c_rating' : s.results.dict()['client']['rating'],
        'c_ispdlavg' : s.results.dict()['client']['ispdlavg'],
        'c_ispulavg' : s.results.dict()['client']['ispulavg'],
        'c_loggedin' : s.results.dict()['client']['loggedin'],
        'c_country' : s.results.dict()['client']['country']
        }

        results = dict(flds)
        results.update(flds_server)
        results.update(flds_client)

        return results
