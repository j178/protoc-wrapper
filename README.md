A Python wrapper around the [`protoc`](https://github.com/protocolbuffers/protobuf) compiler, you can add it to your dev dependencies to make sure its version
is compititable with the [`protobuf`](https://pypi.org/project/protobuf/) runtime.

## Use `protoc-wrapper` in your project

```console
$ uv add 'protoc-wrapper[runtime]==6.30.*' --dev
$ uv run protoc -I <proto path> ...
```

## Run a specific version of `protoc`

```console
$ uv tool run protoc-wrapper --version
```

## TODO

- [ ] Workflow to release new version automatically
