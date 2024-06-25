import requests

def fetchRandom_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)


    if data["success"] and "data" in data:
        userData = data["data"]
        userName = userData["login"]["username"]
        userCountry = userData["location"]["country"]

        return userName, userCountry
    
    else:
        raise Exception("failed to fetch user data")
    

def main():
    try:
        userName, userCountry = fetchRandom_user()
        print(f"Username:{userName} \n Country: {userCountry}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()