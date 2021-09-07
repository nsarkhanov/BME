
from bing_image_downloader import downloader
classeName_file='itemNames.text'
with open(classeName_file,'rt') as f:
	classeNames=f.read().rstrip('\n').split('\n')
	f.close()
# print(len(classeNames))
# print(type(classeNames))
# print(classeNames)
for i in classeNames:
	downloader.download(i, limit=10,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)








# from bing_images import bing
#
# urls = bing.fetch_image_urls("cat", limit=10, file_type='png', filters='+filterui:aspect-square+filterui:color2-bw')
# print("{} images.".format(len(urls)))
# counter = 1
# for url in urls:
#     print("{}: {}".format(counter, url))
#     counter += 1
