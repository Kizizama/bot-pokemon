from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/1.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"
    
    def info(self):
        return f"Имя твоего покемона: {self.name}"

    def show_img(self):
        return self.img

    # Новый метод для кормления покемона
    def feed(self):
        # Можно реализовать увеличение уровня или просто сообщение
        return f"{self.name} накормлен! Он счастлив!"


