package main

import (
	"fmt"
	"net/http"

	"github.com/go-chi/chi"
)
func main() {
	fmt.Println("Server is runnig...")
	r := chi.NewRouter()

	r.Get("/", func(w http.ResponseWriter, r *http.Request){
		w.Write([]byte("welcome"))
	})

	http.ListenAndServe(":3000", r)

}


// import "fmt"

// func main() {
// 	fmt.Println("HEllo")
// }