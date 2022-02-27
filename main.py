import requests
import re


def api():
    api_key = "8743f41d-98c6-4578-9d7b-611af96a16ba"
    response = requests.get("https://ralph.motionlab.io/api/interviewInfo?apiKey=" + api_key)
    if response.status_code == 200:
        response_json = response.json()
        print(f"První volání proběhlo úspěšně, odpověď serveru kód {response.status_code}, výsledek: {response_json}")
    else:
        print(f"Nastala chyba odpovědi serveru - kód {response.status_code}")
        exit(1)
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input("Zadejte email: ")
        if re.fullmatch(regex, email):
            name = input("Zadejte jméno: ")
            send_data = {"email": email, "name": name}
            access_token = response_json['authorization'].get('access_token')
            response2 = requests.post("https://ralph.motionlab.io/api/interviewTest", json=send_data,
                                      headers={"Authorization": f"Bearer {access_token}"})
            if response2.status_code == 200:
                print(f"Poslání dat proběhlo v pořádku - odpověď serveru kód {response2.status_code}.")
                exit(0)
            else:
                print(f"Při odeslání dat nastala chyba odpovědi serveru - kód {response2.status_code}.")
                exit(1)
        else:
            print("Nesprávný email")
            continue


api()
