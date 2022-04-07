from website import create_app
from connectdb import Database

app = create_app()
conn = Database('ksb-2022')

# r = conn.select("select current_date")
# print(r)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
