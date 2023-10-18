import requests

def generate_number():
    response = requests.get('http://apiservice:5000/api')
    data = response.json()
    print(f"Random generated number: {data['number']}")

if __name__ == '__main__':
    generate_number()