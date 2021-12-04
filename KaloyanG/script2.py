if __name__ == "__main__":
    print("Executed as script-program")
else:
    print("Executed as module from another script - name: {}".format(__name__))