from core.app_factory import create_app

app = create_app('test_sql_lite')

if __name__ == '__main__':
    app.run(host='0.0.0.0')