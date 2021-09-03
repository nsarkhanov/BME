from simple_image_download import simple_image_download as simp

classeName_file='itemNames.text'
with open(classeName_file,'rt') as f:
	classeNames=f.read().rstrip('\n').split('\n')
	f.close()
# print(classeNames)
# #
response = simp.simple_image_download

for name in classeNames:
	response().download(keywords = name ,limit = 20 )
