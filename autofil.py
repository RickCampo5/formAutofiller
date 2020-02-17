import json
import os
import unidecode

with open('2007.json') as myfile:
	data = json.load(myfile)

def iterateProjects(year):
	i = 0
	for project in data[year]:
		if not 'Área' in project:
			project['Área'] = '-'
		if not 'Arquitecto' in project:
			project['Arquitecto'] = '-'
		if not 'Ubicación' in project:
			project['Ubicación'] = '-'
		if not 'PM' in project:
			project['PM'] = '-'
		if not 'Categoría1' in project:
			project['Categoría1'] = '-'
		
		project['Categoría1'] = unidecode.unidecode(project['Categoría1'])

		name = project['Proyecto']
		surface = project['Área']
		architect = project['Arquitecto']
		location = project['Ubicación']
		pm = project['PM']
		category = [project['Categoría1'].lower().replace(" ", "-")]
		if 'Categoría2' in project.keys() :
			project['Categoría2'] = unidecode.unidecode(project['Categoría2'])
			category.append(project['Categoría2'].lower().replace(" ", "-"))
		createJSCode(year, name, surface, architect, location, pm, category, i)
		i += 1

def createJSCode(year, name, surface, architect, location, pm, category, i):
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
	fl = os.path.splitext(f'projects{i}.json')[0] + ".js"
	otf = open(fl, 'w')
	otf.writelines(text_arr)
	otf.close()


if __name__ == "__main__":
	iterateProjects('2007')
