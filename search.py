
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
from imutils import build_montages
from imutils import paths
import random

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
ap.add_argument("-s", "--sample", type=int, default=21,
	help="# of images to sample")
args = vars(ap.parse_args())


imagePaths = list(paths.list_images(args["result_path"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]


cd = ColorDescriptor((8, 12, 3))


query = cv2.imread(args["query"])
features = cd.describe(query)


searcher = Searcher(args["index"])
results = searcher.search(features)


cv2.imshow("Query", query)


images = []
 

for (score,resultID) in results:
	
	result = cv2.imread(args["result_path"] + "/" + resultID)
	
	images.append(result)
 

montages = build_montages(images, (128, 196), (3, 6))

for montage in montages:
	cv2.imshow("Search Results", montage)
	cv2.waitKey(0)