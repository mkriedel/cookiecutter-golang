package main

import (
{% if cookiecutter.use_cobra == "y" %}    "bitbucket.orionhealth.global/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/cmd"{% else %}
	"flag"
	"fmt"{% endif %}
)

func main() {

    {% if cookiecutter.use_cobra == "y" %}cmd.Execute(){% else %}
    versionFlag := flag.Bool("version", false, "Version")
	flag.Parse()

	if *versionFlag {
		fmt.Println("Git Commit:", GitCommit)
		fmt.Println("Version:", Version)
		if VersionPrerelease != "" {
			fmt.Println("Version PreRelease:", VersionPrerelease)
		}
		return
	}

	fmt.Println("Hello."){% endif %}
}
