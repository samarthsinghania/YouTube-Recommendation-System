from file_functions import Fily

topics = [
    "Programming",
    "Machine Learning",
    "Artificial Intelligence",
    "Cybersecurity",
    "Web Development",

    "Gaming",
    "Minecraft",
    "Valorant",
    "GTA V",
    "Esports",

    "Technology",
    "Smartphones",
    "PC Building",
    "Gadgets",
    "Tech Reviews",

    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",

    "Finance",
    "Investing",
    "Entrepreneurship",
    "Business",
    "Productivity",

    "Fitness",
    "Bodybuilding",
    "Nutrition",
    "Running",
    "Yoga",

    "Cooking",
    "Pizza",
    "Baking",
    "Home Cleaning",
    "DIY Projects",

    "Travel",
    "Vlogs",
    "Movies",
    "Anime",
    "Music"
]
#GEN THE ACTUAL DATA
obj = Fily()

for query in topics:

    obj.raw_data_gen(query=query, max=50)

    obj.Raw_Data_To_Normal()

