import glob

from plotrdm import plot_rdm

basedir = "."

if __name__ == "__main__":
    count = 0
    for count, path in enumerate(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True)):
        print(f"processing {path}")
        output_image = f'rdm_{count:01}.pdf'
        print(f"output image will be {output_image}")
        plot_rdm(path, output_image)
    print(f"processed {count+1} files")
