
from time import sleep
from copy import deepcopy

  

def Create_Blank_Grid(): #creates a blank grid
  list_of_lists = [] #list of lists
   
  for i in range(30): #runs 30 times for the 30 rows
    row = [] #make a list called row each of those 30 times
    
    for j in range(60): #runs 60 times for 60 columns
      element = False 
      row.append(element) #add a False to the list row 60 times
      
    list_of_lists.append(row) #add row to list_of_lists, and repeat
    
  return list_of_lists #return list_of_lists at the end
    


def Load_Design(file_name, Grid): #function that loads the design
  myFile = open(file_name, "r") #reads the file_name
  
  Coordinates = myFile.read().strip().split() #reads it, then strips white space, and splits by space, not \n
  
  for i in range(0, len(Coordinates), 2):
    Row = int(Coordinates[i]) #for every 2 coordinates, the first would represent the row, and the second would represent the column. set row equal to position index i, but integer.
    
    Column = int(Coordinates[i+1]) #set column equal to position index i+1 (the number right after i), but integer
    
    Grid[Row][Column] = True #index Grid into row first, then index that by column. set that corresponding value true
  
  
  
def Print_Grid(Grid):
  empty = "" #empty string 
  
  for row in Grid: #runs for each row
    for element in row: #runs for each element in the row
    
      if element == False: #if element is false, add a dash
        empty += "-"
        
      elif element == True: #if element is true, add a O
        empty += "O"
    
    empty += "\n" #add \n to separate rows
    
  print(empty) #print the empty string
    


def Check_Neighbors(Row, Col, Grid):
  number = 0
  
  if Row >= 1: #only if row is greater than or equal to 1, can you check top
    if Grid[Row-1][Col] == True: #top cell
      number += 1
      
    if Col < len(Grid[0])-1: #only if col is less than the last (which is len(Grid[0]) -1, can you check right  
      if Grid[Row-1][Col+1] == True: #top right cell
        number += 1
      
    if Col >= 1: #only if col is greater than 1, can you check left 
      if Grid[Row-1][Col-1] == True: #top left cell
        number += 1 
      
     
  if Col >= 1: #only if col is >= 1, can you check left
    if Grid[Row][Col-1] == True: #middle left cell
      number += 1 
  
  if Col < len(Grid[0])-1: #only if col is less than the last, can you check right
    if Grid[Row][Col+1] == True: #middle right cell
      number += 1 
  
  
  if Row < len(Grid)-1: #only if row is less than the last, can you check bottom
    if Grid[Row+1][Col] == True: #bottom middle cell
      number += 1  
      
    if Col >= 1: #only if col is >= 1, can you check left
      if Grid[Row+1][Col-1] == True: #bottom left cell
        number += 1 
  
    if Col < len(Grid[0])-1: #only if col is less than the last, can you check right
      if Grid[Row+1][Col+1] == True: #bottom right cell
        number += 1 
    
  return number #return how many neighbors



def Advance_Cell(Row, Col, Grid):
  neighbors = Check_Neighbors(Row, Col, Grid) #first, call check_neighbors
  
  if Grid[Row][Col] == True: #if the middle cell is a living cell
    if neighbors <= 1: #underpopulation, it dies
      return False 
  
    elif neighbors == 2 or neighbors == 3: #maintains, it lives
      return True 
    
    elif neighbors >= 4: #overpopulation, it dies
      return False 
      
      
  elif Grid[Row][Col] == False: #if the middle cell is dead
    if neighbors == 3: #repopulation, it comes back to life
      return True
      
    else: #otherwise, it remains dead
      return False
    
  
  
def Advance_Grid(Grid): #function to advance the whole grid
  current = deepcopy(Grid) #current grid - made a copy
  
  for i in range(len(Grid)): #for the 30 rows
    for j in range(len(Grid[0])): #60 columns
      Row = i #set the row equal to the current i value
      Col = j #set the column equal to the current j value
      
      
      Grid[Row][Col] = Advance_Cell(Row, Col, current) #we use current because current is the old grid that is not being updated
      
      
  return Grid #then, return the grid





#-------------------------------------------------------    
print("Welcome to Conway's Game of Life! We start with a 30 by 60 grid of cells, either live or dead. Here are the rules:")
print("\n\n1) Any live cell with fewer than two live neighbors dies, by underpopulation")
print("\n2) Any live cell with two or three live neighbors lives on to the next generation")
print("\n3) Any live cell with more than three live neighbors dies, by overpopulation")
print("\n4) Any dead cell with exactly three live neighbors becomes alive, by reproduction")


choice = input("\nPress any key to continue: ")
sleep(1)


Game = []
Game = Create_Blank_Grid()
Load_Design("f-pentomino.in", Game)
Print_Grid(Game)

input("Above is the starting grid. Press any key to start the simulation: ")
sleep(1)


while True:
  Game = Advance_Grid(Game)
  Print_Grid(Game)
  sleep(0.3)






