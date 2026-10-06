package api

import (
	"context"
	"errors"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestResponseLimit(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		chunk := strings.Repeat("x", 8192)
		for i := 0; i <= (64<<20)/len(chunk); i++ {
			if _, err := io.WriteString(w, chunk); err != nil {
				return
			}
		}
	}))
	defer server.Close()
	data, err := New(server.URL).Do(context.Background(), http.MethodGet, "/", nil, nil)
	if err == nil || !strings.Contains(err.Error(), "64 MiB") || data != nil {
		t.Fatalf("oversized response: bytes=%d err=%v", len(data), err)
	}
}

func TestCustomRedirectPolicyAndTransportError(t *testing.T) {
	const token = "dummy-token"
	blocked := errors.New("custom redirect policy " + token)
	client := &http.Client{CheckRedirect: func(req *http.Request, via []*http.Request) error {
		return blocked
	}}
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		http.Redirect(w, r, "/target", http.StatusFound)
	}))
	defer server.Close()
	api := New(server.URL, WithHTTPClient(client), WithAuth("Authorization", "Bearer", token))
	_, err := api.Do(context.Background(), http.MethodGet, "/", nil, nil)
	if !errors.Is(err, blocked) || strings.Contains(err.Error(), token) {
		t.Fatalf("transport error must preserve its cause without its secret: %v", err)
	}
}

func TestSameOriginRedirect(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/start" {
			http.Redirect(w, r, "/target", http.StatusFound)
			return
		}
		if r.Header.Get("Authorization") != "Bearer dummy-token" {
			t.Error("same-origin redirect lost authentication")
		}
		_, _ = io.WriteString(w, "ok")
	}))
	defer server.Close()
	client := New(server.URL, WithAuth("Authorization", "Bearer", "dummy-token"))
	data, err := client.Do(context.Background(), http.MethodGet, "/start", nil, nil)
	if err != nil || string(data) != "ok" {
		t.Fatalf("same-origin redirect: data=%q err=%v", data, err)
	}
}
