import datetime
import redshift_


def get_time():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(current_date)
    return current_date

def get_data(app_id, user_id, os_name):
    conn = redshift_connector.connect(
        host='',
 port=5439,
 database='events',
 user='',
 password=''
 )

    with conn.cursor() as cursor:
        cursor.execute("delete sandbox.events;")
        print('删除 sandbox.events数据')
        cursor.execute(
            "COPY sandbox.events FROM 's3://holla-group-data/log-server/sandbox/raw/{}' iam_role 'arn:aws:iam::529673077012:role/redshiftSpectrumRole' JSON 'auto' GZIP maxerror 10000;".format(get_time()))
        print('数据从s3 copy到 sandbox.events')
        cursor.execute(
            '''select event,attributes,user_properties from sandbox.events where app_id = '{}' and user_id = '{}' and json_extract_path_text(user_properties,'os') in ('{}');'''.format(
                app_id, user_id, os_name))
        print('查数据')
        data = cursor.fetchall()
        print(data)
    return data