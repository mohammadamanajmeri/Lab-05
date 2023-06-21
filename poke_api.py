'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    random_pokemon = get_pokemon_info("pikachu")
    # Use breakpoints to view returned dictionary
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    
    
    pokemon_name = str(pokemon_name).strip().lower()
    headers = {
        'Accept': 'application/json'
    }
    
   
    print(f'Getting information for {pokemon_name}...success\n', end='')
    url = POKE_API_URL + pokemon_name
    resp_msg = requests.get(url, headers=headers)
    print(f'Posting new paste to pastebin...success')


    if resp_msg.status_code == requests.codes.ok:
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
    return

if __name__ == '__main__':
    main()