# 10. Write a program to generate ClassNotFoundException

"""In Python, there's no built-in ClassNotFoundException like in Java. However, you can simulate a similar scenario by attempting to import a module or access an attribute that doesn't exist."""

def generate_class_not_found_exception():
    try:
        import non_existent_module
    except ImportError:
        raise ImportError("Class not found!")

def main():
    try:
        generate_class_not_found_exception()
    except ImportError as e:
        print("Error:", e)

# Main block
if __name__ == "__main__":
    main()
