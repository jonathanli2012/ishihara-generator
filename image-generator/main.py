from run import run_draw
from colors import *
import argparse

if __name__ == "__main__":
    #command line arguments
    parser = argparse.ArgumentParser(description='Ishihara Generator')

    parser.add_argument('mask_image', type=str,
                        help='image must have a white background')

    parser.add_argument('--dots', '-d', type=int,
                        help='specify number of dots requested on canvas (takes a int)')

    """
    parser.add_argument('--save_all', '-s', action='store_true',
                        help='save all images')
    """
    
    args = parser.parse_args()
    if(args.dots == None):
        run_draw(args.mask_image, colors.plate_2_bkg, colors.plate_2_txt)
    elif(args.dots > 0):
        run_draw(args.mask_image, colors.plate_2_bkg, colors.plate_2_txt, dots=args.dots)
    else:
        print("error")
        quit()