import datetime
import logging
import requests
import pyodbc
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    server = 'servername.database.windows.net'
    database = 'databasename'
    username = 'username'
    password = 'password'
    driver= '{ODBC Driver 17 for SQL Server}'

    # Specifying the ODBC driver, server name, database, etc. directly
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

    # Create a cursor from the connection
    cursor = cnxn.cursor()

    # This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
    cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    cnxn.setencoding(encoding='utf-8')

    # Grab JSON Data from API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    json_data = requests.get(url).json()

    # Create empty lists to store the JSON Data
    btc_time = json_data['time']['updatedISO']
    bpi_usd_rate = json_data['bpi']['USD']['rate_float']
    bpi_gbp_rate = json_data['bpi']['GBP']['rate_float']
    bpi_eur_rate = json_data['bpi']['EUR']['rate_float']

    cursor.execute("insert into btctable01(btctimeX, bpi_usd_rateX, bpi_gbp_rateX, bpi_eur_rateX) values (?, ?, ?, ?)", btc_time, bpi_usd_rate, bpi_gbp_rate, bpi_eur_rate)
    cnxn.commit()