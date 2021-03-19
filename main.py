import os
from PIL import Image
import imagehash

# Calculating hashes of sample files
sample_hashes = {}
for sample in os.listdir('samples/'):
    path = 'samples/{}'.format(sample)
    hash = imagehash.average_hash(Image.open(path))
    sample_hashes[sample] = str(hash)

print(sample_hashes)

key_list = list(sample_hashes.keys())
val_list = list(sample_hashes.values())

# For all files under /images path (subdirectories included)
for path, subdirs, files in os.walk('images/'):
    for name in files:
        file_path = os.path.join(path, name)
        file_hash = imagehash.average_hash(Image.open(file_path))
        try:
            # If image matches with one sample files
            match_index = val_list.index(str(file_hash))
            print('"{}" -- matches with --> {}'.format(name, key_list[match_index]))
            # Deleting image file
            os.remove(file_path)
        except ValueError:
            print('No Match Found!')






