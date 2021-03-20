package handler

import (
	"encoding/json"
	"fmt"
	"net/http"

	"GoAPI/Bookstruct"
	"github.com/jinzhu/gorm"
	_"github.com/jinzhu/gorm/dialects/sqlite"
	"github.com/go-chi/chi"
	"time"

)

var db *gorm.DB
var err error
var t = time.Now().Format("02-Jan-2006 15:04:05")

//Initializing the Database
func InitialMigration(){
	db, err = gorm.Open("sqlite3", "test.db")
	if err !=nil{
		fmt.Println(err.Error())
		panic("Failed toconnect to database ")
	}

	defer db.Close()

	db.AutoMigrate(&Bookstruct.Book{})
}

// Getting all the books in the database
func AllBooks(w http.ResponseWriter, r *http.Request){
	db, err = gorm.Open("sqlite3", "test.db")
	if err !=nil{
		fmt.Println(err.Error())
		panic("Failed toconnect to database ")
	}

	defer db.Close()

	var books []Bookstruct.Book
	db.Find(&books)
	json.NewEncoder(w).Encode(books)
}

//Creating a book and storing it to the databse
func BooksCreate(w http.ResponseWriter, r *http.Request){
	db, err = gorm.Open("sqlite3", "test.db")
	if err !=nil{
		fmt.Println(err.Error())
		panic("Failed toconnect to database ")
	}

	defer db.Close()

	title := chi.URLParam(r, "title")
	author := chi.URLParam(r, "author")
	time := t

	db.Create(&Bookstruct.Book{Title:title, Author:author, Time:time})

	fmt.Fprintf(w, "New Book Successfull Created")

}

// Deleting a selected book from the database
func DeleteBook(w http.ResponseWriter, r *http.Request){
	db, err = gorm.Open("sqlite3", "test.db")
	if err != nil{
		fmt.Println("Failedtoconnect to database")
	}

	defer db.Close()

	
	title := chi.URLParam(r, "title")
	author := chi.URLParam(r, "author")

	var book Bookstruct.Book
	
	if err := db.Where("title=?", title).Where("author=?",author).First(&book).Error; err != nil {
		fmt.Fprintf(w, "Book is not on File")
	  }else{
		db.Delete(&book)

		fmt.Fprintf(w, "Book Sucessfully Deleted")

	  }

}


//Updating a book from the datase
//This will need a emmet due to having the previous
// book to update the new book.
func UpdateBook(w http.ResponseWriter, r *http.Request){
	db, err = gorm.Open("sqlite3", "test.db")
	if err != nil{
		fmt.Println("Failedtoconnect to database")
	}

	defer db.Close()

	
	title := chi.URLParam(r, "title")
	author := chi.URLParam(r, "author")

	var book Bookstruct.Book

	if err := db.Where("title=?", title).First(&book).Error; err != nil {
		fmt.Fprintf(w, "Book is not on File")
	  }else{
		
		book.Title = title
		book.Author = author
		db.Save(&book)
		fmt.Fprintf(w, "Book Sucessfully Updated")

	  }

	





	fmt.Fprintf(w, "Sucessfully Updated User")
}




