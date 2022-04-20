# eco_ind.py
# webscraping py file that fetches indicator data


def build_search_url(url: str, stock: str, key: str) -> str:
    '''Build URL'''
        query_parameters = [('apikey', 'key'),('function', 'TIME_SERIES_DAILY')
                            ,('symbol', stock), ('outputsize', 'compact')]

        return url + '/query?' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> dict:
    '''Send url to API and process response.'''

    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def organize(original: dict, start: str, end: str) -> dict:
    ''' Organize JSON dictionary received from API'''
    day = timedelta(days = 1)
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    try:
        new1 = original['Time Series (Daily)']
        dates = OrderedDict()
        while start_date != end_date:
            try:
                dates[start_date.isoformat()] = new1[start_date.isoformat()]
            except:
                pass
            finally:
                start_date += day
        try:
            dates[end_date.isoformat()] = new1[end_date.isoformat()]
        except:
            pass
        return dates
    except:
        print('FAILED')
        print('200')
        print('FORMAT')
        sys.exit()





# insert this key where necessary....

# AXU72VPOM66CY810