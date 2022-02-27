import requests
import re


def api():
    api_key = "8743f41d-98c6-4578-9d7b-611af96a16ba"
    response = requests.get("https://ralph.motionlab.io/api/interviewInfo?apiKey=" + api_key)
    call1_status = response.status_code
    if call1_status == 200:
        call1 = response.json()
        print(f"První volání proběhlo úspěšně, odpověď serveru kód {call1_status}, výsledek: {call1}")
    else:
        print(f"Nastala chyba odpovědi serveru - kód {call1_status}")
        exit(1)
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input("Zadejte email: ")
        if re.fullmatch(regex, email):
            name = input("Zadejte jméno: ")
            send_data = {"email": email, "name": name}
            access_token = call1['authorization'].get('access_token')
            response2 = requests.post("https://ralph.motionlab.io/api/interviewTest", json=send_data,
                                      headers={"Authorization": f"Bearer {access_token}"})
            call2 = response2.status_code
            if call2 == 200:
                print(f"Poslání dat proběhlo v pořádku - odpověď serveru kód {call2}.")
                exit(0)
            else:
                print(f"Při odeslání dat došlo k chybě - odpověď serveru kód {call2}.")
                exit(1)
        else:
            print("Nesprávný email")
            continue


api()
