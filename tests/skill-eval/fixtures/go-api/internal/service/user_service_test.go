package service

import (
	"context"
	"testing"
)

type fakeRepo struct {
	savedName string
}

func (r *fakeRepo) Save(_ context.Context, name string) error {
	r.savedName = name
	return nil
}

func TestCreateUserRejectsBlankName(t *testing.T) {
	repo := &fakeRepo{}
	service := NewUserService(repo)

	err := service.CreateUser(context.Background(), "   ")

	if err == nil {
		t.Fatal("expected an error for blank input")
	}
}
