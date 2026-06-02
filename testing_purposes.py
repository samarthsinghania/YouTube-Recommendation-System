from file_functions import Fily
import json as js

# with open('file.json', 'r') as f:
#     data = js.load(f)



# # print(type(data))
obj = Fily()
# new = obj.Raw_Data_To_Normal(data)
# # print("***NEW DATA****: ",new)
# print(obj.data_appender(new_data=new))


# string = "Hey GUYS$Welcome_BACK_TO_my_Channel_YO"
# print("^" in obj.special)
# print(obj.word_extractor(string.split()))

print(obj.tag_extractor('m0hEJCxojWg'))

# from YoutubeTags import videotags

# video = "https://www.youtube.com/watch?v=m0hEJCxojWg"

# tag = videotags(video).split(",")

# print([item.strip() for item in tag])