from colour import COLOR_NAMES_TO_RGB

#Returns an RGB tuple 
def readColor(color = (0,0,0)):
    #Convert Hex input to tuple
    if color[0] == "#":
        try:
            rgb = color[1:]
            #6 digit Hex
            if len(rgb) == 6:
                r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
            #3 digit Hex
            elif len(rgb) == 3:
                r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
            else:
                raise ValueError()       
        
        #Invalid input given
        except:
            raise ValueError("Invalid value  provided for rgb color.")

        return tuple([float(int(v, 16)) for v in (r, g, b)])

    #Convet string input to tuple
    elif color in COLOR_NAMES_TO_RGB.keys():
        color = COLOR_NAMES_TO_RGB[color]
        return (int (color[0]), int (color[1]), int (color[2]))

    return(0,0,0)

