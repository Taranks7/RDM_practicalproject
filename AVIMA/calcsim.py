import glob

from plotrdm import calc_sim

basedir = "."

if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'similarity_table{count:01}.csv'
        print(f"output image will be {output_image}")
        calc_sim(path, output_image)
    print(f"processed {count} files")
    
from plotrdm import calc_dis    
if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'dissimilarity_table{count:01}.csv'
        print(f"output image will be {output_image}")
        calc_sim(path, output_image)
    print(f"processed {count} files")
    
from plotrdm import corr    
if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'correlation_table{count:01}.csv'
        print(f"output image will be {output_image}")
        corr(path, output_image)
    print(f"processed {count} files")
    
from plotrdm import pos_corr    
if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'postive_correlation_table{count:01}.csv'
        print(f"output image will be {output_image}")
        corr(path, output_image)
    print(f"processed {count} files")
    
    
from plotrdm import neg_corr    
if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'negative_correlation_table{count:01}.csv'
        print(f"output image will be {output_image}")
        corr(path, output_image)
    print(f"processed {count} files")
