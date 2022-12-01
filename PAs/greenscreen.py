###
### Author: Tom Giallanza
### Class: CSC 110
### Description: ?
###

def validate():
    '''This function prompts the user for various settings about the greenscreen process.
    If one of these inputs are invalid, the program tells the user and exits. Once all of the inputs
    are received, they are returned by the function.
    Parameters: None
    '''
    channel = input('Enter color channel\n')
    if channel == "r" or channel == "g" or channel == "b":
        channel_difference = input('Enter color channel difference\n')
        if 1 <= float(channel_difference) <= 10: 
            gs_file = input('Enter greenscreen image file name\n')
            fi_file = input('Enter fill image file name\n')
            if get_image_dimensions_string(gs_file) == get_image_dimensions_string(fi_file):
                out_file = input('Enter output file name\n')
                print("Output file written. Exiting.")
                return channel, channel_difference, gs_file, fi_file, out_file
            else:
                print("Images not the same size. Will exit.")
                exit()
        else:
            print("Invalid channel difference. Will exit.")
            exit()
    else:
        print("Channel must be r, g, or b. Will exit.")
        exit()

def process_file(loaded_gs_file, fi_file, channel, channel_difference):
    '''This function takes in the loaded gs_file and puts the image data through the algorithm, comparing it to the
    fi_file. If the selected color (or channel) of the pixel of the gs_file is greater than or equal to that color of the 
    corresponding pixel in the fi_file times the channel_difference, then it is replaced by the file in the fi_file. The resulted
    data is added to a new string and finally returned at the end of the function. 
    Parameters: loaded_gs_file can be a list
    fi_file can be a string
    channel can be a string
    channel_difference can be a float
    '''
    result = ""
    row_index = 0
    for row in loaded_gs_file:
        pixel_index = 0
        for pixel in row:
            fi_pixel = load_image_pixels(fi_file)[row_index][pixel_index]
            if channel == "r":
                if pixel[0] > (pixel[1] * channel_difference) and pixel[0] > (pixel[2] * channel_difference):
                    pixel[0] = fi_pixel[0]
                    pixel[1] = fi_pixel[1]
                    pixel[2] = fi_pixel[2]
            elif channel == "g":
                if pixel[1] > (pixel[0] * channel_difference) and pixel[1] > (pixel[2] * channel_difference):
                    pixel[0] = fi_pixel[0]
                    pixel[1] = fi_pixel[1]
                    pixel[2] = fi_pixel[2]
            else:
                if pixel[2] > (pixel[0] * channel_difference) and pixel[2] > (pixel[1] * channel_difference):
                    pixel[0] = fi_pixel[0]
                    pixel[1] = fi_pixel[1]
                    pixel[2] = fi_pixel[2]
            result += str(pixel[0]) + " " + str(pixel[1]) + " " + str(pixel[2]) + " "
            pixel_index += 1
        result += "\n"
        row_index += 1
    return result

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def main():
    '''This function uses the initial parameters from the validate function and opens the files which are being analyzed.
    The process_file function then processes the data and checks which pixels need to be replaced. The returned pixel data
    for the new sample image is returned and then written into the new sample file, creating a "greenscreen" effect.
    '''
    channel, channel_difference, gs_file, fi_file, out_file = validate()
    float_channel_difference = float(channel_difference)
    loaded_gs_file = load_image_pixels(gs_file)
    opened_out_file = open(out_file, "w")
    opened_out_file = open(out_file, "a")
    opened_out_file.write("P3\n" + get_image_dimensions_string(gs_file) + "\n" + "255\n")
    result = process_file(loaded_gs_file, fi_file, channel, float_channel_difference)
    opened_out_file.write(result)

main()

