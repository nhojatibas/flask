from app import manager
#server = Server(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    print("Main..: "+str(__name__))
    #manager.run(host="0.0.0.0", port=int("5000"), debug=True)
    manager.run()
