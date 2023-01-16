from plotter import *
from GUI import *
def main():
    try:
        start()
    except Exception as e:
        print("A critical error has occured, please restart the program.")
        print(f"Error: {e}")
        return

if __name__ == '__main__':
    main()
