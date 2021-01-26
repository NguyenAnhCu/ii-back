##############################################################################
# package description  and copyrights go here
#
#
#
##############################################################################


import cv2 
import numpy as np

class image :
    def __init__(self, image_height, image_width, 
            background_color=(255,255,255), frame_color=(181,142,0), 
            shape_color_1=(241, 241, 182), shape_color_2=(112, 91, 43)):
        """
        Contructor of class image
        @params 
            @image_height : type int 
                            description lenght of image
            @image_width : type : int
                            description width of image
        """
        self.__width = image_width
        self.__height = image_height
        self.image = np.zeros([self.__width,self.__height,3],dtype=np.uint8)
        self.image[:,:,:] = np.array(background_color)
        self._box_color = frame_color
        self._shapes_color = shape_color_1
        self._shapes_color_2 = shape_color_2

    def create_frame(self, size, x_position, y_position, color=(181,142,0), thick=-1 ):
        """
        this function create a box from 2 points fill with the chose color
        @params :
        @size : type : tuple or list
                        height and width of box
        @x_position : type : int
                        x coordinate of the box
        @y_position : type : int
                        y coordinate of the box
        @color : type : tuple or list
                        color of the box
        @thick : type : int
                        thickness of the box
        @ return None
        """
        self.image = cv2.rectangle(self.image, (x_position, y_position), 
                         (x_position + size[1], y_position + size[0]), 
                            color, thickness=thick)
    
    def sub_frame(self, image, size, x_position, y_position, color=(181,142,0), thick=-1):
        """
        Create a square shape frame
        @params :
        @size : type : tuple or list
                        height and width of box
        @x_position : type : int
                        x coordinate of the box
        @y_position : type : int
                        y coordinate of the box
        @color : type : tuple or list
                        color of the box
        @thick : type : int
                        thickness of the box
        @ return None
        """
        return cv2.rectangle(image, (x_position, y_position), 
                    (x_position + size[0], y_position + size[1]), color, thickness=thick)

    def add_h_lines(self, pos_x, pos_y, distance, thickness=2, color=(240,240,0)):
        """ draw a vertical line

        @params
        self: self
            the image on which line is to be drawn
        pos_x: int
            x-axis of the starting point
        pos_y: int
            y-axis of the starting point
        distance: int
            distance from the starting point
        thickness: int
            line thickness
        color=(240, 240, 0)
            line color
        """
        self.image = cv2.line(self.image, (pos_x, pos_y), (pos_x+distance, pos_y), self._shapes_color, thickness)

    def add_sub_h_lines(self, image ,pos_x, pos_y, distance, thickness=2, color=(240,240,0)):
        """ draws a horizontal line
        @params
        @self: self
               the image on which line is to be drawn
        @pos_x: int
                x-axis of the starting point
        @pos_y: int
                y-axis of the starting point
        @distance: int
                   distance from the starting point
        @thickness: int
                    line thickness
        @color=(240, 240, 0)
                line color
        """
        return cv2.line(image, (pos_x, pos_y), (pos_x+distance, pos_y), self._shapes_color, thickness)
     
    def add_v_lines(self, pos_x, pos_y, distance, thickness=2, color=(240,240,0)):
        """ draws a vertical line
        @params
        @self: self
               the image on which line is to be drawn
        @pos_x: int
                x-axis of the starting point
        @pos_y: int
                y-axis of the starting point
        @distance: int
                   distance from the starting point
        @thickness: int
                    line thickness
        @color=(240, 240, 0)
                line color
        """
        self.image = cv2.line(self.image, (pos_x, pos_y), (pos_x, pos_y+distance), self._shapes_color, thickness)

    def init_question(self,  start_x, start_y, box_size, number_of_boxes=3):
        self.pos_x = start_x
        self.pos_y = start_y
        self.box_height = box_size[0]
        self.box_width = box_size[1]
        self.number_of_boxes = number_of_boxes

    def draw_question_boxes(self):
        """
        Draw a 3 * 3 grid
        @params
        @self
        """
        size = (self.box_height ,self.box_width)
        pos_x = self.pos_x
        for _ in range(self.number_of_boxes):
            pos_y = self.pos_y
            for _ in range (self.number_of_boxes):
                self.create_frame(size, pos_x, pos_y, color=self._box_color)
                self.create_frame((size[0]+4, size[1]+4), pos_x-2, pos_y-2, color=(0,0,0), thick=2)
                pos_y += size[1] + 5
            pos_x += size[0] + 5

    def save_question_info(self, path):
        """
        Save an image to a given path
        @params
            @self: self
            @path: string
                   path to save the file
        """
        question_label = cv2.imread("../data/ques.png")
        question_label = cv2.resize(question_label, (self.box_height,self.box_width)) 
        x_response = self.pos_x  + (self.box_height * 2) + 10
        y_response = self.pos_y + (self.box_height * 2) + 10
        response = self.image[y_response:y_response+self.box_width, x_response:x_response+self.box_height,:]
        cv2.imwrite(path + "true_response.png", response)
        self.image[y_response:y_response+self.box_width, x_response:x_response+self.box_height] = question_label


    def draw_triangle(self, pt1, pt2, pt3, color=(240,240,0), thickness = -1):
        """
        Draw a triangle
        @params
            @self: self
            @path: string
                   path to save the file
            @color: array of int
                    line array
            @thickness: int
                        line thickness
        """
        triangle_cnt = np.array( [pt1, pt2, pt3] )
        cv2.drawContours(self.image, [triangle_cnt], 0, color, thickness)


    def draw_hexagon(self, centre, size, color_indexs):
        """
        Draw an hexagon (composed of 6 triangles)
        @params
        @self: self

        @center: int

        @size:

        @color_indexs:
        """
        color_list=(self._shapes_color_2, self._shapes_color)
        pt1 = centre

        pt2 = (centre[0] - size, centre[1] + (2*size))
        pt3 = (centre[0] + size, centre[1] + (2*size))
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[0]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)

        pt2 = (centre[0] - size , centre[1] + (2*size))
        pt3 = (centre[0] - (2*size), centre[1])
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[1]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)

        pt2 = (centre[0] - 2*size , centre[1])
        pt3 = (centre[0] - size, centre[1] - 2*size)
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[2]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)

        pt2 = (centre[0] - size , centre[1]- 2*size)
        pt3 = (centre[0] + size, centre[1] - 2*size)
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[3]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)

        pt2 = (centre[0] + size , centre[1]- 2*size)
        pt3 = (centre[0] + 2*size, centre[1])
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[4]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)

        pt2 = (centre[0] + size , centre[1]+ 2*size)
        pt3 = (centre[0] + 2*size, centre[1])
        self.draw_triangle(pt1, pt2, pt3, color_list[color_indexs[5]])
        self.draw_triangle(pt1, pt2, pt3, self._shapes_color,1)


    def save_image(self, path):
        """
        save an image to a given path
        @params
            @self: self
            @path: string
                   path to save the file
        """
        cv2.imwrite(path, self.image)

    def show(self, window_name):
        """
        display on a window
        @params
            @self: self
            @window_name: image
            ?????????????????????????????????????????????????????
        """
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)