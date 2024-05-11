# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:42:16 2023

@author: ANIKET
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:02:53 2023

@author: ANIKET
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 01:09:15 2023

@author: ANIKET
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:22:59 2023

@author: ANIKET
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import math
import numpy as np
import matplotlib.pyplot as plt
from tkinter import simpledialog

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        

        # Button to open image
        open_button = tk.Button(self.root, text="Open Image", command=self.open_image)
        open_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        gray_button = tk.Button(self.root, text="Show gray", command=self.apply_gray)
        gray_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        histogram_button = tk.Button(self.root, text="Histogram", command=self.apply_histogram)
        histogram_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        

        # Button to apply negative effect
        negative_button = tk.Button(self.root, text="Apply Negative", command=self.apply_negative)
        negative_button.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        # Button to apply pseudo effect
        pseudo_button = tk.Button(self.root, text="Apply Pseudo", command=self.apply_pseudo)
        pseudo_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        
        # Button to apply threshold effect
        threshold_button = tk.Button(self.root, text="Apply Threshold", command=self.apply_threshold)
        threshold_button.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        
     
        
        

        # Label to display the selected image
        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=1, column=0, columnspan=5, pady=10)

        self.selected_image_path = None
        self.output_image_path = "D://IIT Bombay//Projects//modified_target_image_50.jpg"
        
    

    def open_image(self):
        self.selected_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        # Display the selected image
        if self.selected_image_path:
            image = Image.open(self.selected_image_path)
            image = ImageTk.PhotoImage(image)
            self.image_label.configure(image=image)
            self.image_label.image = image
            
            
    def apply_histogram(self):
        if self.selected_image_path:
            # Call the negative function with the selected image
            self.histogram(self.selected_image_path, self.output_image_path)

            # Open another window for the modified image
            modified_window = tk.Toplevel(self.root)
            modified_window.title("Histogram")
            self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

            # Display the modified image
            
            modified_image = Image.open(self.output_image_path)
            modified_image = ImageTk.PhotoImage(modified_image)
            modified_label = tk.Label(modified_window, image=modified_image)
            modified_label.image = modified_image
            modified_label.pack()
            
       
    def gray(self, image_path, output_path):
        if self.selected_image_path:
            image = Image.open(self.selected_image_path)
            grayscale_image = image.convert('L')
            grayscale_image.save(output_path)
           
        
    def apply_gray(self):
        if self.selected_image_path:
            # Call the negative function with the selected image
            self.gray(self.selected_image_path, self.output_image_path)

            # Open another window for the modified image
            modified_window = tk.Toplevel(self.root)
            modified_window.title("Gray Image")
            self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

            # Display the modified image
            
            modified_image = Image.open(self.output_image_path)
            modified_image = ImageTk.PhotoImage(modified_image)
            modified_label = tk.Label(modified_window, image=modified_image)
            modified_label.image = modified_image
            modified_label.pack()
            

    def apply_negative(self):
        if self.selected_image_path:
            # Call the negative function with the selected image
            self.negative(self.selected_image_path, self.output_image_path)

            # Open another window for the modified image
            modified_window = tk.Toplevel(self.root)
            modified_window.title("Negative Image")
            self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

            # Display the modified image
            modified_image = Image.open(self.output_image_path)
            grayscale_modified_image = modified_image.convert('L')
            modified_image_tk = ImageTk.PhotoImage(grayscale_modified_image)
            modified_label = tk.Label(modified_window, image=modified_image_tk)
            modified_label.image = modified_image_tk
            modified_label.pack()
            
            """
            modified_image = ImageTk.PhotoImage(modified_image)
            modified_label = tk.Label(modified_window, image=modified_image)
            modified_label.image = modified_image
            modified_label.pack()"""
            
    def apply_pseudo(self):
        if self.selected_image_path:
            # Call the negative function with the selected image
            self.pseudo(self.selected_image_path, self.output_image_path)

            # Open another window for the modified image
            modified_window_pseudo = tk.Toplevel(self.root)
            modified_window_pseudo.title("Pseudo Image")
            self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

            # Display the modified image
            modified_image_pseudo = Image.open(self.output_image_path)
            modified_image_pseudo = ImageTk.PhotoImage(modified_image_pseudo)
            modified_label_pseudo = tk.Label(modified_window_pseudo, image=modified_image_pseudo)
            modified_label_pseudo.image = modified_image_pseudo
            modified_label_pseudo.pack()
    
    def apply_threshold(self):
        if self.selected_image_path:
            # Call the negative function with the selected image
            self.threshold(self.selected_image_path, self.output_image_path)

            # Open another window for the modified image
            modified_window_threshold = tk.Toplevel(self.root)
            modified_window_threshold.title("Threshold Image")
            self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
            
            #user_input = simpledialog.askstring("Input", "Enter something:")

            # Display the modified image
            modified_image_threshold = Image.open(self.output_image_path)
            modified_image_threshold = ImageTk.PhotoImage(modified_image_threshold)
            modified_label_threshold = tk.Label(modified_window_threshold, image=modified_image_threshold)
            modified_label_threshold.image = modified_image_threshold
            modified_label_threshold.pack()
            
    def threshold(self, image_path, output_path):
        image = Image.open(image_path)
        #image = image.convert('L')
        
        # new line of code
        #image = gray(image)
        
        threshold_input = simpledialog.askstring("Input", "Enter comma-separated thresholds:")
        threshold_values = [int(value.strip()) for value in threshold_input.split(',')]
        
        threshold_1 = threshold_values[0]
        threshold_2 = threshold_values[1]
        threshold_3 = threshold_values[2]
        
        width, height = image.size
        pixel_values = []

        for y in range(height):
            for x in range(width):
                val = image.getpixel((x, y))
                pixel_values.append(val[0])

        unique_pixel_values = list(set(pixel_values))
        unique_pixel_values.sort()

        pixel_levels = unique_pixel_values
        pixel_levels_count = [pixel_values.count(level) for level in pixel_levels]

        I_min, I_max = min(pixel_levels), max(pixel_levels)
        O_min, O_max = 0, 255

        newly_mapped_numerator = O_max - O_min
        newly_mapped_denominator = I_max - I_min

        newly_mapped_levels = [
            ((newly_mapped_numerator / newly_mapped_denominator) * (i - I_min)) + O_min
            for i in pixel_levels
            ]

        pixels = image.load()
        mapper = {key: math.ceil(value) for key, value in zip(pixel_levels, newly_mapped_levels)}

        for y in range(height):
            for x in range(width):
                val = image.getpixel((x, y))
                initial_value = val[0]
                new_value = mapper[initial_value]

                if 0 <= new_value <= threshold_1:
                    c = 50
                elif threshold_1 < new_value <= threshold_2:
                    c = 90
                elif threshold_2 < new_value <= threshold_3:
                    c = 150
                else:
                    c = 210

                pixels[x, y] = (c, c, c)

        image.save(output_path)

            
    def pseudo(self, image_path, output_path):
        image = Image.open(image_path)
        
        # new line of code 
        #image = gray(image)
        
        width, height = image.size
        
        threshold_input = simpledialog.askstring("Input", "Enter comma-separated levels:")
        threshold_values = [int(value.strip()) for value in threshold_input.split(',')]
        
        threshold_1 = threshold_values[0]
        threshold_2 = threshold_values[1]
        
        
        color_input = simpledialog.askstring("Input", "Enter comma-separated RGB levels:")
        color_values = [int(value.strip()) for value in color_input.split(',')]
        
        color_1 = color_values[0]
        color_2 = color_values[1]
        color_3 = color_values[2]
        pixel_values = []

        for y in range(height):
            for x in range(width):
                val = image.getpixel((x, y))
                pixel_values.append(val[0])

        unique_pixel_values = list(set(pixel_values))
        unique_pixel_values.sort()

        pixel_levels = unique_pixel_values
        pixel_levels_count = [pixel_values.count(level) for level in pixel_levels]

        I_min, I_max = min(pixel_levels), max(pixel_levels)
        O_min, O_max = 0, 255

        newly_mapped_levels = [
            ((O_max - O_min) / (I_max - I_min)) * (i - I_min) + O_min
            for i in pixel_levels
            ]

        pixels = image.load()
        mapper = {key: math.ceil(value) for key, value in zip(pixel_levels, newly_mapped_levels)}

        for y in range(height):
            for x in range(width):
                val = image.getpixel((x, y))
                initial_value = val[0]
                new_value = mapper[initial_value]

                if 0 <= new_value < threshold_1:
                    a, b, c = 200, 0, 0
                elif threshold_1 <= new_value < threshold_2:
                    a, b, c = 0, 190, 0
                else:
                    a, b, c = 0, 0, 250

                pixels[x, y] = (math.ceil(a), math.ceil(b), math.ceil(c))

        image.save(output_path)


    def negative(self, image_path, output_path):
        # Open the image
        original_image = Image.open(image_path)
        # new line of code
        #original_image = gray(original_image)

        # Get image dimensions
        width, height = original_image.size

        # Create a blank image with the same size
        negative_image = Image.new('RGB', (width, height))

        # Invert the colors (negative effect)
        for x in range(width):
            for y in range(height):
                pixel = original_image.getpixel((x, y))
                inverted_pixel = tuple(255 - value for value in pixel)
                negative_image.putpixel((x, y), inverted_pixel)

        # Save the negative image
        negative_image.save(output_path)
        
        
    
    def histogram(self, image_path, output_path):
        image = Image.open(image_path)
        width, height = image.size
        pixel_values = []
        for row in range(width):
            for column in range(height):
                val = image.getpixel((row, column))
                pixel_values.append(val[0])
        unique_pixel_values = []
        for i in pixel_values:
            if i not in unique_pixel_values:
                unique_pixel_values.append(i)
        
        unique_pixel_values.sort()
        pixel_levels = unique_pixel_values
        pixel_levels_count = []
        for level in pixel_levels:
            count = pixel_values.count(level)
            pixel_levels_count.append(count)
        frequency = pixel_levels_count
        plt.bar(pixel_levels, frequency)
        plt.xlabel("Pixel level (0 to 255)")
        plt.ylabel("Pixel frequency")
        plt.title("Histogram")
        plt.savefig(output_path)
        
    
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
