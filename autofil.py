import json
import os

with open('projects2.json') as myfile:
 data = json.load(myfile)

def iterateProjects(year, i):
 	name = data[year][i]['Proyecto']
 	surface = data[year][i]['Área']
 	architect = data[year][i]['Arquitecto']
 	location = data[year][i]['Ubicación']
 	pm = data[year][i]['PM']
 	category = [data[year][i]['Categoría1']]
 	if 'Categoría2' in data[year][i].keys() :
 		category.append(data[year][i]['Categoría2'])
 	createJSCode(year, name, surface, architect, location, pm, category)

def createJSCode(year, name, surface, architect, location, pm, category):
 	text_arr = []
 	text_arr.append(f"document.getElementById('name').value = '{name}';\n")
 	text_arr.append(f"document.getElementById('input').value = '{year}';\n")
 	text_arr.append(f"document.getElementById('size').value = '{surface}';\n")
 	text_arr.append(f"document.getElementById('architect').value = '{architect}';\n")
 	text_arr.append(f"document.getElementById('location').value = '{location}';\n")
 	text_arr.append(f"document.getElementById('pm').value = '{pm}';\n")
 	text_arr.append("var categoryLength = document.getElementById('category').options.length;\n")
 	text_arr.append("var elemCategory = document.getElementById('category');\n")
 	text_arr.append(f"var categories = {category};\n")
 	text_arr.append("for(var i = 0; i < categoryLength; i++) {\n")
 	text_arr.append("elemCategory.options[i].selected = categories.indexOf(elemCategory.options[i].value) >= 0;\n")
 	text_arr.append("};\n")
 	fl = os.path.splitext('projects2.json')[0] + ".js"
 	otf = open(fl, 'w')
 	otf.writelines(text_arr)
 	otf.close()


if __name__ == "__main__":
 	iterateProjects('2015', 0)
