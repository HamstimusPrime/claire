from functions.get_file_content import get_file_content

def test_main():
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "lorem.txt"))


    
if __name__ == "__main__":
    test_main()