A Python wrapper around the [`protoc`](https://github.com/protocolbuffers/protobuf) compiler, you can add it to your dev dependencies to make sure its version
is compititable with the [`protobuf`](https://pypi.org/project/protobuf/) runtime.

## Use `protoc-wrapper` in your project

```console
$ uv add 'protoc-wrapper==30.2' --dev
$ uv add 'protobuf==6.30.2'
$ uv run protoc -I <proto path> ...
```

## Run a specific version of `protoc`

```console
$ uvx protoc-wrapper@30.2 --version
```

## TODO

- [ ] Workflow to release new version automatically
- [X] Support prereleases
