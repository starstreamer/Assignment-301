ITEMS = {
    'John greased ': ['axle', 'wheel', 'wheels', 'wheel', 'engine', ''],
    'Paul alleged ': ['truth', 'crime', 'facts', 'infidelity', 'incident', ''],
    'Tracy freed ': ['animals', 'fish', 'slaves', 'slaves', 'slaves', 'pizza'],
    'Lisa plowed ': ['field', 'field', '', '', '', ''],
}

for key, value in sorted(ITEMS.items()):
    print(key, len([item for item in value if item]))
#
# for each in data:
#     i = 0
#     print each
#     for item in data[each]:
#         if len(item) > 0:
#             i =i +1
#     print i
#
# List = ['Mon','Mon','Mon','Mon']
# result = True
# # Get the first element
# first_element = List[0]
# # Compares all the elements with the first element
# for word in List:
#    if first_element != word:
#       result = False
#       count+=1
#       print("All elements are not equal")
#       break
#    else:
#       result = True
#    if result:
#       print("All elements are equal")
#

#for key, value in ITEMS.items():
    #print value


 #   print(key, len([item for item in value if item]))