from datetime import datetime
import os
import requests
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.ecommerce.models.customer import DimCustomer



def GetCustomerData():
    customers =[]
    for i in range(1396):
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        if response.status_code==200:
            user_info = response.json()
            data = user_info["results"][0]
            customer = {}
            customer["name"]=data["name"]["first"] + " " + data["name"]["last"]
            customer["email"]=data["email"]
            customer["address"]=data["location"]["street"]["name"] + ", " + data["location"]["city"] + ", " + data["location"]["state"] + ", " + data["location"]["country"]
            customer["phone"]=data["phone"]
            customer["picture_url"]=data["picture"]["medium"]
            customer["registration_date"]=data["registered"]["date"]
            customer["gender"]=data["gender"]
            customers.append(customer)
    return customers

def LoadCustomer(customers):
    dotenv.load_dotenv()
    # Step 1: Load environment variables from .env file
    # load_dotenv()

    # Step 2: Retrieve database connection details from environment variables
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')

    # Step 3: Create the connection string
    connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)
    # Step 5: Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for cus in customers:
            registration_date = datetime.fromisoformat(cus["registration_date"].replace("Z", "+00:00"))
            print("inserting data")
            cust = DimCustomer(
                name=cus["name"],
                email=cus["email"],
                address=cus["address"],
                phone=cus["phone"],
                registration_date=registration_date,
                picture_url=cus["picture_url"],
                gender=cus["gender"]
                )
            session.add(cust)
        session.commit()
    except Exception as ex:
        print("exception part")
        print(f"Error loading customer data: {ex}")
        session.rollback()
    finally:
        print("closing session")
        session.close()

