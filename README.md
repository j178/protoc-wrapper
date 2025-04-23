A Python wrapper around the [`protoc`](https://github.com/protocolbuffers/protobuf) compiler, you can add it to your dev dependencies to make sure its version
is compititable with the [`protobuf`](https://pypi.org/project/protobuf/) runtime.

```console
$ uv add 'protoc-wrapper==6.30.*' --dev
$ uv add 'protobuf==6.30.*'
$ uv run protoc -I <proto path> ...
```
