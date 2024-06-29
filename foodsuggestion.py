class FoodSuggester:
    def __init__(self):
        self.food_optionsaz = [
            {"name": "Pizza", "price": 10},
            {"name": "Burgers", "price": 8},
            {"name": "Salad", "price": 6},
            {"name": "Pasta", "price": 12},
            {"name": "Sushi", "price": 15},
            {"name": "Taco", "price": 7},
        ]

    def suggest_foodaz(self, budgetaz):
        suggestionsaz = [foodaz for foodaz in self.food_optionsaz if foodaz["price"] <= budgetaz]
        return suggestionsaz

def main():
    food_suggesteraz = FoodSuggester()
    budgetaz = float(input("Enter your budget: "))
    suggestionsaz = food_suggesteraz.suggest_foodaz(budgetaz)

    if suggestionsaz:
        print("Based on your budget, you can afford the following foods:")
        for foodaz in suggestionsaz:
            print(f"- {foodaz['name']} (${foodaz['price']})")
    else:
        print("Sorry, no food options available within your budget.")

if __name__ == "__main__":
    main()
