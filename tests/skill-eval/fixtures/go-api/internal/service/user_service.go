package service

import (
	"context"
	"errors"
	"strings"
)

type UserRepository interface {
	Save(ctx context.Context, name string) error
}

type UserService struct {
	repo UserRepository
}

func NewUserService(repo UserRepository) *UserService {
	return &UserService{repo: repo}
}

func (s *UserService) CreateUser(ctx context.Context, name string) error {
	if name == "" {
		return errors.New("name is required")
	}

	return s.repo.Save(ctx, strings.TrimSpace(name))
}
