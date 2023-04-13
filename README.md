#### Native Planet software version server

Serves a JSON blob with current version information for all software.

Gets updated by authenticated webhook called by Jenkins build jobs.

Caches data in sqlite db.

```json
{
  "groundseg": {
    "canary": {
      "groundseg": {
        "amd64_sha256": "e486d6000c109fc15a3b5c3328d297042daf26c306fac0cc1072fd2f4426f49a",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_rc2-v1.1.18_latest",
        "arm64_sha256": "4e48526d0891aebe3de3e79a61f3581d7b0b45b04f76aafb3aa3b88e5e1e3f52",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_rc2-v1.1.18_latest",
        "major": 1,
        "minor": 1,
        "patch": 18
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
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "6ece7c64c4396dd3ca9db4044d2c029c1ab8869f05e046241f81174ba4b949a2",
        "arm64_sha256": null,
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "edge"
      },
      "webui": {
        "amd64_sha256": "a814c8e6e1b2095e818e2432710eeed45378fb83e6b818961379885c8d587b21",
        "arm64_sha256": "b52b1735eb88aa0da5d00b0898bc358b41de2cdf31f54ac6b8885902ceb913b9",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "latest"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    },
    "edge": {
      "groundseg": {
        "amd64_sha256": "e486d6000c109fc15a3b5c3328d297042daf26c306fac0cc1072fd2f4426f49a",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_rc2-v1.1.18_edge",
        "arm64_sha256": "4e48526d0891aebe3de3e79a61f3581d7b0b45b04f76aafb3aa3b88e5e1e3f52",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_rc2-v1.1.18_edge",
        "major": 1,
        "minor": 1,
        "patch": 18
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
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "44b188a9c465b9eedd9f2a091a5c31235ed1c729499f9449902974a8a1e3007b",
        "arm64_sha256": "b1de9cba6ab695999cf4925b14a5208ddb0f2217e7e9f8f0a7db09bf1d69f118",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v2.1"
      },
      "webui": {
        "amd64_sha256": "a814c8e6e1b2095e818e2432710eeed45378fb83e6b818961379885c8d587b21",
        "arm64_sha256": "b52b1735eb88aa0da5d00b0898bc358b41de2cdf31f54ac6b8885902ceb913b9",
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
        "amd64_sha256": "e486d6000c109fc15a3b5c3328d297042daf26c306fac0cc1072fd2f4426f49a",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_rc2-v1.1.18_latest",
        "arm64_sha256": "4e48526d0891aebe3de3e79a61f3581d7b0b45b04f76aafb3aa3b88e5e1e3f52",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_rc2-v1.1.18_latest",
        "major": 1,
        "minor": 1,
        "patch": 18
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
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "8c759f85d43168c0afaf550c0a4a614445d34838b710db7ad6fc7d61b0abc96a",
        "arm64_sha256": "b28e760c4e4f3bd0f6bf7604dc7a4a01751cb058c0b10a5c769419eda756a147",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v2.1"
      },
      "webui": {
        "amd64_sha256": "a814c8e6e1b2095e818e2432710eeed45378fb83e6b818961379885c8d587b21",
        "arm64_sha256": "b52b1735eb88aa0da5d00b0898bc358b41de2cdf31f54ac6b8885902ceb913b9",
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