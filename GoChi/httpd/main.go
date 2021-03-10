package main

import (
	
	"fmt"
	"main/pkg/newsfeed"
	"main/httpd/handler"
	"net/http"

	"github.com/go-chi/chi"
)
func main() {
	
	port := ":3000"


	feed := newsfeed.New()
	r := chi.NewRouter()

	r.Get("/newsfeed", handler.NewsfeedGet(feed))
	
	r.Post("/newsfeed", handler.NewsfeedPost(feed))

	fmt.Println("Serving on " + port)
	http.ListenAndServe(port, r)
	
}


// import "fmt"

// func main() {
	// 	fmt.Println("HEllo")
	// r.Get("/", func(w http.ResponseWriter, r *http.Request){
	// 	w.Write([]byte("welcome"))
	// })
// }