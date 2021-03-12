package Bookstruct

type Getter interface{
	GetAll() []Book
}

type Adder interface{
	Add(book Book)

}

type Book struct{
	Title string `json:"title`
	Author string `json:"author`
	Time string `json:"time`

}

type Repo struct{
	Books []Book
}

func New() *Repo{
	return &Repo{
		Books: []Book{},
	}
}

func(r *Repo) Add(book Book){
	r.Books = append(r.Books, book)
}

func(r *Repo) GetAll() []Book{
	return r.Books
}