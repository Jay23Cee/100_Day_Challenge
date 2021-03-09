package main

import (
	"encoding/json"
	"fmt"
	"main/pkg/newsfeed"
	"net/http"

	"github.com/go-chi/chi"
)
func main() {
	fmt.Println("Server is runnig...")
	feed := newsfeed.New()
	r := chi.NewRouter()

	r.Get("/newsfeed", func(w http.ResponseWriter, r *http.Request) {
		items := feed.GetAll()
		json.NewEncoder(w).Encode(items)



	})
	
	r.Post("/newsfeed", func(w http.ResponseWriter, r *http.Request){

	})

	http.ListenAndServe(":3000", r)
	
}


// import "fmt"

// func main() {
	// 	fmt.Println("HEllo")
	// r.Get("/", func(w http.ResponseWriter, r *http.Request){
	// 	w.Write([]byte("welcome"))
	// })
// }