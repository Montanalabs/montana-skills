package http

import (
	"net/http"
)

type UserService interface {
	CreateUser(r *http.Request, name string) error
}

type UserHandler struct {
	service UserService
}

func (h *UserHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if err := h.service.CreateUser(r, name); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusCreated)
}
