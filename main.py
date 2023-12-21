import requests
import base64
def get_prediction(image_data):
  url = 'https://askai.aiclub.world/ce326c5d-7454-48f6-81c0-73f2a1a771fa'
  r = requests.post(url, data=image_data)
  response = r.json()['predicted_label']
  print(response)
  return response

score = 0

while True:
    country = input('Which car brand is from the country Japan? toyota, renault, fiat, volkswagen: ')

    if country == "toyota":
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is toyota')

    country = input('Which car brand is from the country France? mercedes-benz, ferrari, ds, suzuki: ')

    if country == "ds":
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is ds')

    country = input('Which car brand is from the country Italy? audi, maserati, alpine, subaru: ')

    if country == "maserati":
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is maserati')

    country = input('Which car brand is from the country Germany? nissan, bugatti, lamborghini, bmw: ')

    if country == "bmw":
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is bmw')

    country = input('Which car brand is from the country Russia? bmw, toyota, Isuzu, Lada: ')

    if country == 'Lada':
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is Lada')

    country = input('Which car brand is from The US? Suzuki, Ford, Benz, Chery: ')

    if country == 'Ford':
        print('You are correct!')
        score += 1
    else:
        print('You are incorrect! Answer is Ford')

    country = input('Which car has the legendary Rotary engine? Mazda 3, Toyota supra, Tesla Model S, Mazda RX8: ')

    if country == 'Mazda RX8':
        print('You are correct!')
        score += 1

    print(f'Your current score is {score}')
    play_again = input('Do you want to play again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print(f"Thank you for playing! Your final score is {score}. Goodbye!")






  

