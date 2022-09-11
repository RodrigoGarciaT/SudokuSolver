import requests

url = "https://sudoku-board.p.rapidapi.com/new-board"

querystring = {"diff": "2", "stype": "list", "solu": "true"}

headers = {
    "X-RapidAPI-Key": "ae5dfb3c2amsh0245873f3cc2ae5p1dd10cjsn99b478674369",
    "X-RapidAPI-Host": "sudoku-board.p.rapidapi.com"
}


def generate_sudoku():
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response['response']['unsolved-sudoku']
