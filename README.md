# image-search-engine
In this project, an image query is accepted through a command line interface & the algorithm performs searching and ranking for similar images.


Steps to build Image Search Engine:
Step 1: Define your descriptor. What type of descriptor (how to represent images using only a list of numbers known as feature vectors) are you going to use? Are you describing color, texture, shape?

Step 2: Indexing Dataset. After selecting a descriptor, it will be applied to extract features from each and every image in our dataset. The process of extracting features from an image is called "indexing". These features are then written to disk for later use. Indexing is also a task that's easily made parallel by utilizing multiple cores/processors on your machine.

Step 3: Defining Similarity Metric. In step 1, we defined a method to extract features from an image. Now, we need to define a method to compare our feature vectors. A distance function should accept two feature vectors and then return a value indicating how "similar" they are. Common choice for similarity functions include (but are certainly not limited to) Euclidean, Manhattan, Cosine and Chi-squared distances.

Step 4: Searching. To perform a search, apply your descriptor to your query image, and then ask your distance metric to rank how similar your images are in your index to your query images. Sort your results via similarity and then examine them.
