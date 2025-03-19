print("*****************Welcome to the World of Books********************")
Name=input("Enter your Full Name:")
yob=int(input("Enter your yob: (for ex:1990)"))
Age=2025-yob
if Age>18:
    book_type=input("Choose your Favourite book_type:(Comics,Horror,Poetic)")
    if book_type=="Comics":
        Comic_author=input("Choose your Favourite Comic_author:(Franklin,Robics)")
        if Comic_author=="Franklin" or "Robics":
            print("Have your Favourite Book:",book_type,Comic_author)
        
    
    
    