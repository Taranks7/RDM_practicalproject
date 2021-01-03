import glob

from displotrdm import calc_dissim

basedir = "."

if __name__ == "__main__":
    count = 0
    for count, path in enumerate(sorted(glob.glob(f'{basedir}/**/Meadow*.json', recursive=True))):
        print(f"processing {path}")
        count +=1
        output_image = f'dis_rdm_{count:02}.pdf'
        print(f"output image will be {output_image}")
        calc_dissim(path, output_image)
    print(f"processed {count} files")
