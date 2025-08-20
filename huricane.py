#Name: Daniel Lavdari
#Date: November 26, 2024
# Hurricane turtle


import turtle
import pandas as pd

def setup(windowTitle):
    screen = turtle.Screen()
    screen.title(windowTitle)
    screen.setup(800, 404)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("mapNASA.gif")
    t = turtle.Turtle()
    t.penup()
    t.pensize(1)
    t.color()
    return t, screen


def animate(t, lat, lon, wind):
    if t is None:
        print("Error: Turtle object is None.")
        return
    t.goto(lon, lat)
    if wind > 157:
        t.color("red")
        t.pensize(5)
    elif 130 <= wind <= 156:
        t.color("orange")
        t.pensize(4)
    elif 111 <= wind <= 129:
        t.color("yellow")
        t.pensize(3)
    elif 96 <= wind <= 110:
        t.color("green")
        t.pensize(2)
    elif 74 <= wind <= 95:
        t.color("blue")
        t.pensize(1)
    else:
        t.color("white")
        t.pensize(1)
    t.pendown()
    return(t)

def main():
    hFile = input("Enter file name: ")
    t, wn = setup(hFile)
    try:
        df = pd.read_csv(hFile)
    except FileNotFoundError:
        print(f"Error: File '{hFile}' not found.")
        return
    for index, row in df.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]
        animate(t, lat, lon, wind)
    wn.mainloop()


if __name__ == "__main__":
    main()


