
def replacetext(search_text, replace_text, file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(data)
    return (file_name + " Replaced !")


file_names = ["package.json", "package-lock.json"]

for file_name in file_names:
    print(replacetext("the-via/keyboards", "WestBerryVIA/keyboards", file_name))

print("Replace done!")
