from functions.write_file import write_file

def test_main():
    print (write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print (write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print (write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    
if __name__ == "__main__":
    test_main()