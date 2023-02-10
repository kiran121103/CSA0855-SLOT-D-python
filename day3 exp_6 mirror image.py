def mirror_image(num):
    num_str = str(num)
    return int(num_str[::-1])

num =input("Enter the str: ")
mirror = mirror_image(num)
print("Mirror image:", mirror)
