target "build" {
  dockerfile = "Dockerfile"
  tags = ["favelalvara/calculadora-docker:latest"]
  args = {
    FOO = "bar"
  }
}

target "validate-build" {
  inherits = ["build"]
  call = "check"
}