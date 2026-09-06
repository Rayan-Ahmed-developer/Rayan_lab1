# Travel Agent - Lab 1
# Simple rule-based travel agent for Google Colab

def travel_agent():
    print("===== Smart Travel Agent =====")

    destination = input("Enter your destination: ")
    budget = float(input("Enter your total budget (PKR): "))
    days = int(input("Enter number of travel days: "))
    activity = input("Preferred activity (beach/mountains/culture/adventure): ").lower()

    # Simple estimated daily costs
    daily_costs = {
        "beach": 8000,
        "mountains": 7000,
        "culture": 6000,
        "adventure": 9000
    }

    daily_cost = daily_costs.get(activity, 7000)
    estimated_cost = daily_cost * days

    print("\n===== Travel Recommendation =====")
    print("Destination:", destination)
    print("Days:", days)
    print("Preferred activity:", activity)
    print("Estimated trip cost: PKR", estimated_cost)
    print("Your budget: PKR", budget)

    if estimated_cost <= budget:
        print("Status: Suitable")
        print("Recommendation: Your trip is within your budget.")
    else:
        extra = estimated_cost - budget
        print("Status: Over budget")
        print("You need approximately PKR", extra, "more.")
        print("Recommendation: Reduce trip days or choose a lower-cost activity.")

    print("\nTravel Agent completed successfully!")


travel_agent()
