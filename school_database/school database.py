# def get_location(coordinates, commands):
#
#     new_coordinates = coordinates
#
#     for comand in commands:
#         if comand =="forward":
#             new_coordinates[1] += 1
#         elif comand =="right":
#             new_coordinates[0] += 1
#         elif comand =="left":
#             new_coordinates[0] -= 1
#         else:
#             new_coordinates[1] -= 1
#
#     return new_coordinates
#
# get_location([0, 0], ["forward", "right"])


obj = object(x = 10, y =10)

print(obj)