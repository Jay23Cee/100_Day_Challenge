package main

import ( 
	"fmt"
	"log"
	"net/http"
	"github.com/gorilla/mux"
)

func helloWorld(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Hello World")
}

func handleRequest(){
	myRouter := mux.NewRouter().StrictSlash(true)
	myRouter.HandleFunc("/", helloWorld).Methods("GET")
	myRouter.HandleFunc("/users", AllUsers).Methods("GET")
	myRouter.HandleFunc("/users/{name}/{email}", NewUser).Methods("POST")
	myRouter.HandleFunc("/users/{name}", DeleteUser).Methods("Delete")
	myRouter.HandleFunc("/users/{name}/{email}", UpdateUser).Methods("PUT")

	log.Fatal(http.ListenAndServe(":3000", myRouter))
}


func main(){
	fmt.Println("GO ORM Tutorial")

	InitialMigration()

	handleRequest()
}

