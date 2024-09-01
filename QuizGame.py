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

correctAns = [2,1,3,2,3,3,1,2,2,1]

ansNumber = 1
indexNum = 0
score = 0

for nation in countries:
    isNumber = False

    print(f"What is the capital of {nation['country']}?:")

    for city in nation['cities']:
        print(f"Option {ansNumber}: {city}")
        ansNumber += 1

    while isNumber == False:
        try:
            isNumber = True
            ans = int(input("\nOption: "))
        except ValueError:
            print("Please enter a number between 1 and 3")
            isNumber = False

    if ans == correctAns[indexNum]:
        score += 1
    
    indexNum +=1
    ansNumber = 1
    print("\n")

print(f"Score:{score}/10")
