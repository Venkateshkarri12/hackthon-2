import random

# Updated sample data with 10 crops
crops = {
    "Wheat": {"soil_type": "Loamy", "season": "Winter"},
    "Rice": {"soil_type": "Clay", "season": "Monsoon"},
    "Maize": {"soil_type": "Sandy", "season": "Summer"},
    "Barley": {"soil_type": "Loamy", "season": "Spring"},
    "Soybean": {"soil_type": "Loamy", "season": "Summer"},
    "Cotton": {"soil_type": "Sandy", "season": "Monsoon"},
    "Potato": {"soil_type": "Clay", "season": "Winter"},
    "Tomato": {"soil_type": "Loamy", "season": "Spring"},
    "Sugarcane": {"soil_type": "Clay", "season": "Summer"},
    "Peanut": {"soil_type": "Sandy", "season": "Summer"}
}

soils = {
    "Loamy": {"pH": 6.5, "nutrients": "Nitrogen, Phosphorus, Potassium"},
    "Clay": {"pH": 5.5, "nutrients": "Nitrogen, Potassium"},
    "Sandy": {"pH": 6.0, "nutrients": "Phosphorus, Potassium"}
}

diseases = {
    "Wheat": ["Rust", "Powdery Mildew"],
    "Rice": ["Bacterial Blight", "Blast"],
    "Maize": ["Maize Streak Virus", "Rust"],
    "Barley": ["Leaf Blotch", "Net Blotch"],
    "Soybean": ["Soybean Cyst Nematode", "Frogeye Leaf Spot"],
    "Cotton": ["Boll Rot", "Leaf Curl Virus"],
    "Potato": ["Late Blight", "Early Blight"],
    "Tomato": ["Tomato Yellow Leaf Curl Virus", "Blossom End Rot"],
    "Sugarcane": ["Red Rot", "Smut"],
    "Peanut": ["Leaf Spot", "Rust"]
}

# Functions for different features
def crop_selection(soil_type, season):
    suitable_crops = [crop for crop, details in crops.items() 
                      if details["soil_type"] == soil_type and details["season"] == season]
    if suitable_crops:
        print(f"Suitable crops for {soil_type} soil and {season} season: {', '.join(suitable_crops)}")
    else:
        print(f"No suitable crops found for {soil_type} soil and {season} season.")

def soil_management(soil_type):
    if soil_type in soils:
        soil = soils[soil_type]
        print(f"Soil Type: {soil_type}")
        print(f"pH Level: {soil['pH']}")
        print(f"Nutrients: {soil['nutrients']}")
        print("Recommended Fertilizers: Organic compost, Manure")
    else:
        print("Soil type not recognized.")

def disease_identification(crop_name):
    if crop_name in diseases:
        print(f"Common diseases for {crop_name}: {', '.join(diseases[crop_name])}")
    else:
        print("Crop not recognized.")

def weather_forecasting():
    weather_conditions = ["Sunny", "Rainy", "Cloudy", "Stormy"]
    forecast = random.choice(weather_conditions)
    print(f"Weather Forecast for Today: {forecast}")
    if forecast == "Rainy":
        print("Recommendation: Delay irrigation and consider drainage measures.")
    elif forecast == "Sunny":
        print("Recommendation: Proceed with irrigation if required.")
    elif forecast == "Stormy":
        print("Recommendation: Secure crops and minimize outdoor activities.")
    else:
        print("Recommendation: Regular farming activities can continue.")

# Main program loop
def main():
    while True:
        print("\nCrop and Soil Management System")
        print("1. Crop Selection Guidance")
        print("2. Soil Management")
        print("3. Disease Identification")
        print("4. Weather Forecasting")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            soil_type = input("Enter soil type (Loamy, Clay, Sandy): ").capitalize()
            season = input("Enter season (Winter, Monsoon, Summer, Spring): ").capitalize()
            crop_selection(soil_type, season)
        elif choice == '2':
            soil_type = input("Enter soil type (Loamy, Clay, Sandy): ").capitalize()
            soil_management(soil_type)
        elif choice == '3':
            crop_name = input("Enter crop name: ").capitalize()
            disease_identification(crop_name)
        elif choice == '4':
            weather_forecasting()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
