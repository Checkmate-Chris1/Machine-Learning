import tkinter as tk

class DataGui:
    def __init__(self, master, length1, length2, length3, length4, length5):
        self.master = master
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
        self.length4 = length4
        self.length5 = length5

        # Create a Canvas widget
        self.canvas = tk.Canvas(master, width=2000, height=500, background="grey")
        self.canvas.pack()

        # Draw the rectangles in rows
        self.draw_rectangles(1)

    def draw_rectangles(self, visual_multiplier):
        """Draw the rectangles with their current lengths and labels."""
        startX = 1000

        # Clear any previous rectangles and text
        self.canvas.delete("all")

        # Draw three rectangles placed in rows
        self.canvas.create_rectangle(startX, 25, startX + self.length1, 75, fill="blue")
        self.canvas.create_rectangle(startX, 125, startX + self.length2, 175, fill="green")
        self.canvas.create_rectangle(startX, 225, startX + self.length3, 275, fill="red")
        self.canvas.create_rectangle(startX, 325, startX + self.length4, 375, fill="yellow")
        self.canvas.create_rectangle(startX, 425, startX + self.length5, 475, fill="black")

        # And value labels to the rectangles
        self.canvas.create_text(startX + self.length1 + 25, 50, text=str(self.length1/visual_multiplier), anchor="w", font=("Arial", 12))
        self.canvas.create_text(startX + self.length2 + 25, 150, text=str(self.length2/visual_multiplier), anchor="w", font=("Arial", 12))
        self.canvas.create_text(startX + self.length3 + 25, 250, text=str(self.length3/visual_multiplier), anchor="w", font=("Arial", 12))
        self.canvas.create_text(startX + self.length4 + 25, 350, text=str(self.length4/visual_multiplier), anchor="w", font=("Arial", 12))
        self.canvas.create_text(startX + self.length5 + 25, 450, text=str(self.length5/visual_multiplier), anchor="w", font=("Arial", 12))

        # Add name labels next to the rectangles
        self.canvas.create_text(30, 50, text="Weight 1 (x)", anchor="w", font=("Arial", 12))
        self.canvas.create_text(30, 150, text="Weight 2 (x^2)", anchor="w", font=("Arial", 12))
        self.canvas.create_text(30, 250, text="Weight 3 (x^3)", anchor="w", font=("Arial", 12))
        self.canvas.create_text(30, 350, text="Weight 4 (x^4)", anchor="w", font=("Arial", 12))
        self.canvas.create_text(30, 450, text="Bias (y-int)", anchor="w", font=("Arial", 12))

def main():
    # Declare three variables to represent the initial lengths of the rectangles
    length1 = 50
    length2 = 100
    length3 = 150
    length4 = 150
    length5 = 25

    # Create the main window
    root = tk.Tk()
    root.title("Summary of Perceptron Data")

    # Pass the lengths to the RectangleApp
    app = DataGui(root, length1, length2, length3, length4, length5)

    # Function to update the rectangles every 3 seconds
    def update_and_wait():
        app.length1 += 50  # Update the rectangles
        app.length2 += 50
        app.length3 += 50
        app.length4 += 50
        app.length5 += 50
        app.draw_rectangles(1)

        root.after(3000, update_and_wait)  # Call update_and_wait again after 3 seconds

    # Start the periodic updates
    update_and_wait()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
