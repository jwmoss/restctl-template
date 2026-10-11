//go:build live

package tests

import (
	"context"
	"encoding/json"
	"os"
	"os/exec"
	"path/filepath"
	"testing"
	"time"
)

func TestLiveReadOnly(t *testing.T) {
	if os.Getenv("{{ cookiecutter.env_prefix }}_LIVE") != "1" {
		t.Fatal("set {{ cookiecutter.env_prefix }}_LIVE=1 after configuring the real API")
	}
	binary := filepath.Join(t.TempDir(), "cli.exe")
	if output, err := exec.Command("go", "build", "-o", binary, "../cmd/{{ cookiecutter.binary_name }}").CombinedOutput(); err != nil {
		t.Fatalf("build CLI: %v\n%s", err, output)
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
	defer cancel()
	query := func(args ...string) []byte {
		t.Helper()
		output, err := exec.CommandContext(ctx, binary, append([]string{"--dry-run", "--json"}, args...)...).Output()
		if err != nil {
			t.Fatalf("live %v failed: %v; verify the configured API and credentials", args, err)
		}
		return output
	}
	var health struct {
		OK bool `json:"ok"`
	}
	if err := json.Unmarshal(query("doctor"), &health); err != nil || !health.OK {
		t.Fatal("live doctor did not confirm API connectivity")
	}
	var resources []struct {
		ID string `json:"id"`
	}
	if err := json.Unmarshal(query("{{ cookiecutter.resource_name_plural }}", "list"), &resources); err != nil || resources == nil {
		t.Fatal("live resource list did not return a JSON array")
	}
	for _, resource := range resources {
		if resource.ID == "" {
			t.Fatal("live resource list contains a resource without an ID")
		}
	}
}
