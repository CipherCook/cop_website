# import sqlite3
# import pandas as pd
# import random

# resto = pd.read_csv("zomato.csv")
# connection = sqlite3.connect("restaurant.db")

# with open('schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()
# # cur.execute("INSERT INTO restaurants (restaurant_name, restaurant_location) VALUES (?, ?)",
# #             (resto['name'][0], resto['address'][0]))

# for i in range(50):
#     c = random.randint(1, 20)
#     avg = random.randint(1, 5)
#     s = avg*c
#     cur.execute("INSERT INTO restaurants (restaurant_name, restaurant_location, restaurant_rating_sum, restaurant_rating_count) VALUES (?, ?, ?, ?)",
#             (resto['name'][i], resto['address'][i], s, c))
    
# cur.execute("INSERT INTO menus (image_url, food_name, food_price, restaurant_id, food_type) VALUES (?, ?, ?, ?, ?)",
#             ("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9vZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", "sushi", 60, 1, "starter"))


# connection.commit()
# connection.close()

# import sqlite3

# import pandas as pd
# import random
# resto = pd.read_csv("zomato.csv")
# food = pd.read_csv("food.csv")

# connection = sqlite3.connect('restaurant.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# for i in range(50):
#     c = random.randint(1, 20)
#     avg = random.randint(1, 5)
#     s = avg*c
#     cur.execute("INSERT INTO restaurants (restaurant_name, restaurant_location, restaurant_rating_sum, restaurant_rating_count) VALUES (?, ?, ?, ?)",
#             (resto['name'][i], resto['address'][i], s, c))


# cur.execute("INSERT INTO menus (image_url, food_name, food_price, restaurant_id, food_type) VALUES (?, ?, ?, ?, ?)",
#             ("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9vZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", "sushi", 60, 1, "starter"))

# for i in range(1,51):
#     increment = random.randint(0, 100)
#     for j in range(1,6):
#         res_id = i
#         item = random.randint(0,24)
#         price = int(food['Price'][item] + increment)
#         url = food['Url'][item]
#         name = food['Item_name'][item]
#         ftype = food['Category'][item]
#         cur.execute("INSERT INTO menus (restaurant_id, food_type, food_name, food_price, image_url) VALUES (?, ?, ?, ?, ?)",(res_id, ftype, name, price, url))


# connection.commit()
# connection.close()

from sqlalchemy import create_engine, text
user = 'root'
password = 'Prathamagra27#'
host = 'LAPTOP-N2DLHE8V'
port = 3306
database = 'restaurant'
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        ),
        connect_args={
            "ssl":{
                "ssl_ca":"/etc/ssl/certs/ca-certificates.crt"
            }
        }
    )
engine = get_connection()
with engine.connect() as conn:
    result = conn.execute(text("select * from restaurants"))
    print(result.all())

# if __name__ == '__main__':
 
#     try:
       
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)