#### Native Planet software version server

Serves a JSON blob with current version information for all software.

Gets updated by authenticated webhook called by Jenkins build jobs.

Caches data in sqlite db.

```json
{
  "groundseg": {
    "edge": {
      "groundseg": {
        "amd64_sha256": "7b8419d0519157bffb4c926f28065b254e3301cc444473270407675595297692",
        "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_edge-v1.1.3_edge",
        "arm64_sha256": "6480738919d01970ca650e4679da0766bffbed5ab11b4cd98b3537e1fc0f5426",
        "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_edge-v1.1.3_edge",
        "major": 1,
        "minor": 1,
        "patch": 3
      },
      "minio": {
        "amd64_sha256": "f6a3001a765dc59a8e365149ade0ea628494230e984891877ead016eb24ba9a9",
        "arm64_sha256": "567779c9f29aca670f84d066051290faeaae6c3ad3a3b7062de4936aaab2a29d",
        "repo": "registry.hub.docker.com/minio/minio",
        "tag": "latest"
      },
      "miniomc": {
        "amd64_sha256": "6ffd76764e8ca484de12c6ecaa352db3d8efd5c9d44f393718b29b6600e0a559",
        "arm64_sha256": "6825aecd2f123c9d4408e660aba8a72f9e547a3774350b8f4d2d9b674e99e424",
        "repo": "registry.hub.docker.com/minio/mc",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "8a407ed5cdf1a1dfd5d096eba33d3ba989e36f7eed9d941642eec8cd459a2276",
        "arm64_sha256": "9adc440389ede681e65e049bdebff33fa8e4c5ec20c728343d74b76b96d5e587",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v1.22"
      },
      "webui": {
        "amd64_sha256": "f6348dd4174deae2ce8ad81e32171278b7d5e4cae2ff08cf1f834bdc5cc1621f",
        "arm64_sha256": "8c47e40b71e6c6c6788d7105e92b1bc7fc3fb72dfcef47f9d4d007d08c529785",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "edge"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    },
    "latest": {
      "groundseg": {
        "amd64_sha256": "fc89fca9df2c0cda2e4435cb58e07ce8eb7b564577033383c8949e0efe6955d6",
        "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_v1.0.8_latest",
        "arm64_sha256": "b3894158f295269f2d12ee3e9039248272c5879df43005a876ba99c43de940d1",
        "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_v1.0.8_latest",
        "major": 1,
        "minor": 0,
        "patch": 8
      },
      "minio": {
        "amd64_sha256": "f6a3001a765dc59a8e365149ade0ea628494230e984891877ead016eb24ba9a9",
        "arm64_sha256": "567779c9f29aca670f84d066051290faeaae6c3ad3a3b7062de4936aaab2a29d",
        "repo": "registry.hub.docker.com/minio/minio",
        "tag": "latest"
      },
      "miniomc": {
        "amd64_sha256": "6ffd76764e8ca484de12c6ecaa352db3d8efd5c9d44f393718b29b6600e0a559",
        "arm64_sha256": "6825aecd2f123c9d4408e660aba8a72f9e547a3774350b8f4d2d9b674e99e424",
        "repo": "registry.hub.docker.com/minio/mc",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "99b811d0ff5dfe70e9bca79d852ccb16b4b598587a8b75ea7b7580ca53b34cbc",
        "arm64_sha256": "cf98ad81eeada04262383333380f5cd1f88c26c47c65275c360f300b6ed6f784",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v1.21"
      },
      "webui": {
        "amd64_sha256": "226335a6c3b41046cd4122a1c8cddd66b75ea76efca39de7b04be684ea2354ec",
        "arm64_sha256": "fdf3592698b60956e8a78ca7f8c70346268be955a5522b39a4c36eb20aa37f91",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "latest"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    }
  }
}
```