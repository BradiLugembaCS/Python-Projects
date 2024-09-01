countries = [
    {"country": "United States", "cities": ["New York", "Washington, D.C.", "Los Angeles"]},
    {"country": "Japan", "cities": ["Tokyo", "Osaka", "Kyoto"]},
    {"country": "France", "cities": ["Marseille", "Lyon", "Paris"]},
    {"country": "Australia", "cities": ["Sydney", "Canberra", "Melbourne"]},
    {"country": "Brazil", "cities": ["São Paulo", "Rio de Janeiro", "Brasília"]},
    {"country": "Canada", "cities": ["Toronto", "Vancouver", "Ottawa"]},
    {"country": "Germany", "cities": ["Berlin", "Munich", "Hamburg"]},
    {"country": "India", "cities": ["Mumbai", "Delhi", "Bangalore"]},
    {"country": "Italy", "cities": ["Venice", "Rome", "Milan"]},
    {"country": "South Africa", "cities": ["Cape Town", "Johannesburg", "Pretoria"]}
]


for nation in countries:
    print(f"What is the capital of {nation['country']}?:")
