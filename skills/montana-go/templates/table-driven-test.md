# Table-driven test template (montana-go)

```go
func TestThing(t *testing.T) {
    tests := []struct {
        name string
        in   string
        want string
        wantErr bool
    }{
        {name: "ok", in: "x", want: "y"},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := DoThing(tt.in)
            if (err != nil) != tt.wantErr {
                t.Fatalf("err=%v wantErr=%v", err, tt.wantErr)
            }
            if got != tt.want {
                t.Fatalf("got=%q want=%q", got, tt.want)
            }
        })
    }
}
```

