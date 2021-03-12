package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"GoAPI/Bookstruct"
	"GoAPI/httpd/handler"
	"github.com/go-chi/chi"
	"github.com/go-chi/chi/v5/middleware"
)

func helloWorld(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World")

}

func handleRequest() {
	port := ":3000"
	feed := Bookstruct.New()
	t := time.Now()

	feed.Add(Bookstruct.Book{
		Title:  "Hello",
		Author: "Jackson",
		Time:t.Format("01-22-2019"),
	})

	r := chi.NewRouter()

	// a good base midwarestack


	//Set a timeout value on the request context (ctx), that will signal
	//through ctx.Done() that the request has timed out and further
	// processing should be stopped.

	r.Use(middleware.Timeout(60 * time.Second))

	r.Get("/", helloWorld)
	r.Get("/Books", handler.AllBooks)
	r.Post("/Books/{title}/{author}", handler.BooksCreate)
	fmt.Println("Serving on" + port)
	log.Fatal(http.ListenAndServe(port, r))

}

func main() {
	fmt.Println("Go Book API starting...")

	handler.InitialMigration()
	handleRequest()

}
