
# from bing_images import bing
#
# urls = bing.fetch_image_urls("cat", limit=10, file_type='png', filters='+filterui:aspect-square+filterui:color2-bw')
# print("{} images.".format(len(urls)))
# counter = 1
# for url in urls:
#     print("{}: {}".format(counter, url))
#     counter += 1
from bing_image_downloader import downloader
downloader.download(query_string, limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
