web={
    'header':'header.html',
    'footer':'footer.html',
    'content':''
}

def anyfunction(x:float,y:int):
    """any descriptive information

    Args:
        x (float): pass in any array called x
        y (int): pass in any array called y

    Returns:
        float: returns the multiplication of x and y
    """
    return x*y

def readfile(filename:str):
    with open(filename, "r") as file_handle:
        file_contents = file_handle.read()
        
  