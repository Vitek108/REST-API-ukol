import requests
import re


def API():
    api_key = "8743f41d-98c6-4578-9d7b-611af96a16ba"
    response = requests.get("https://ralph.motionlab.io/api/interviewInfo?apiKey=" + api_key)
    call1 = response.json()
    print(call1)
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input("Zadejte email: ")
        if re.fullmatch(regex, email):
            name = input("Zadejte jméno: ")
            senddata = {"email": email, "name": name}
            access_token = call1['authorization'].get('access_token')
            response2 = requests.post("https://ralph.motionlab.io/api/interviewTest", json=senddata,
                                      headers={"Authorization": f"Bearer {access_token}"})
            call2 = response2.status_code
            if call2 == 200:
                print(f"Poslání dat proběhlo v pořádku - odpověď serveru kód {call2}.")
                break
            else:
                print(f"Při odeslání dat došlo k chybě - odpověď serveru kód {call2}.")
        else:
            print("Nesprávný email")
            continue


API()
