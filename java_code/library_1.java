import java.util.ArrayList;

class Book{
    public String name, author;
    public Book (String name , String author){
        this.name=name;
        this.author = author;
    }
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Book{" + "name = " + name + "\\" + " aurthor " + author + '}';
    }
}

class Library{
    public ArrayList<Book>books;
    public Library(ArrayList<Book> books){
        this.books = books;
    }
    public void addbook (Book book){
        this.books.add(book);
        System.out.println("the books has been added to the library");
        this.books.add(book);
    
    }

    public void issuebook (Book book , String issue_to){
        this.books.add(book);
        System.out.println("the books has been issued from the library to " + issue_to);
        this.books.remove(book);
    }



    public void returnBook(Book b , String returned_by){
        System.out.println("your book has been returned by " + returned_by);
        this.books.add(b);
    }
}




public class library_1 {
    public static void main(String[] args) {

        ArrayList<Book> bk = new ArrayList<>();
        Book b1 = new Book("algo1", "CL1");
        bk.add(b1);
        Book b2 = new Book("algo2", "CL2");
        bk.add(b2);
        Book b3 = new Book("algo3", "CL3");
        bk.add(b3);
        Book b4 = new Book("algo4", "CL4");
        bk.add(b4);
        
        Library l =new Library(bk);
        l.addbook(new Book("algo1", "author1"));
        System.out.println(l.books);
        l.issuebook(b3, "Domino");

        l.returnBook(b3, "Domino");
        
    }
    
}
