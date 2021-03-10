package handler

import (
	"encoding/json"
	"main/pkg/newsfeed"
	"net/http"
)


func NewsfeedGet(feed newsfeed.Getter) http.HandlerFunc{
	return func(w http.ResponseWriter, r *http.Request) {
		items := feed.GetAll()
		json.NewEncoder(w).Encode(items)



	}
}

